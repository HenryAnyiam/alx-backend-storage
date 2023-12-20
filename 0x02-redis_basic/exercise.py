#!/usr/bin/env python3
"""A module using redis"""


from uuid import uuid4
import redis
from typing import Union, Optional, Callable


class Cache:
    """implementing the redis"""

    def __init__(self) -> None:
        """class initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
