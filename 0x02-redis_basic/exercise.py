#!/usr/bin/env python3
"""A module using redis"""


from uuid import uuid4
import redis
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count function calls"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """function call history"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""

        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """display the history of a particular function"""

    key = method.__qualname__
    redis_cache = redis.Redis()
    input_key = key + ":inputs"
    output_key = key + ":outputs"

    inputs = redis_cache.lrange(input_key, 0, -1)
    outputs = redis_cache.lrange(output_key, 0, -1)

    calls = redis_cache.get(key).decode('utf-8')
    print(f"{key} was called {calls} times:")

    for i, o in zip(inputs, outputs):
        i = i.decode('utf-8')
        o = o.decode('utf-8')

        print(f"{key}(*{i}) -> {o}")


class Cache:
    """implementing the redis"""

    def __init__(self) -> None:
        """class initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores given data using a generated key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """rewrites the default redis.get"""

        value = self._redis.get(key)

        if value is not None:
            if fn:
                value = fn(value)
            return value
        else:
            return None

    def get_str(self, val: bytes) -> str:
        """returs str representation of val"""
        return str(val, val.decode('utf-8'))

    def get_int(self, val: bytes) -> int:
        """returns int representation of val"""
        val = int(val, val.decode('utf-8'))

        return val if val else 0
