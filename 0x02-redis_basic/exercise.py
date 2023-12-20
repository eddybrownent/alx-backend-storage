#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from uuid import uuid4
import redis
from typing import Union, Callable, Optional, Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes,
                                                    int, float, None]:
        """
        Retrieve data from Redis using the given key

        Args:
            key: key of the data in redisDB
            fn: function to convert retrived data. None is default

        Returns:
            The retrieved data, converted by the function with
        """
        value = self._redis.get(key)

        if value is not None and fn is not None:
            return fn(value)

        return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        gets string from redis using the given key

        Args:
            key: the key holding the string in redisdb

        Return:
            The retrieved string or None if key doesnt exist
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Union[int, None]:
        """
        Gets the int from redis using the given key

        Args:
            key: key related to the integer in Redis

        Return:
            the retrieved integer or None if key doesnt exist
        """
        return self.get(key, int)
