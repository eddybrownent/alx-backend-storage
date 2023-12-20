#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from uuid import uuid4
import redis
from typing import Union


class Cache:
    """
    Initialize Cache class with
    Redis client instance & flush the Redis db
    """
    def __init__(self):
        # instance of redis and flush the DB
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, int, float, str]) -> str:
        """
        Store data in Redis with randomly generated key

        Args:
            data: The data to be stored

        Returns:
            str: randomly generated key
        """
        # create a random key and return it
        key = str(uuid4())

        self._redis.set(key, data)

        return key
