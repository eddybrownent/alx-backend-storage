#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    Initialize Cache class with
    Redis client instance & flush the Redis db
    """
    def __init__(self):
        # instance of redis and flush the DB
        r_host = 'localhost'
        r_port = 6379
        r_db = 0
        self._redis = redis.Redis(host=r_host, port=r_port, db=r_db)
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
        key = str(uuid.uuid4())

        self._redis.mset({key: data})

        return key
