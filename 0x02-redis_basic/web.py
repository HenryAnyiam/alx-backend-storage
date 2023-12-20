#!/usr/bin/env python3
""" implement a web cache and tracker"""


import redis
import requests
from functools import wraps
from typing import Callable


_redis = redis.Redis()


def count_request(method: Callable) -> Callable:
    """tracks number of time a URL was accessed in the key"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        """Wrapper function"""

        url = str(*args)
        _redis.incr(f"count:{url}")
        cache = _redis.get(f"count:{url}")

        if cache:
            return cache.decode('utf-8')
        else:
            html = method(url)
            _redis.setex("count:", 10, html)
        return html

    return wrapper


@count_request
def get_page(url: str) -> str:
    """Get HTML content from the URL"""

    result = requests.get(url)
    return result.text
