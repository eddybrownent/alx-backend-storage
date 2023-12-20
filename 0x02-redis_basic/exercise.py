#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from uuid import uuid4
import redis
from typing import Union, Callable, Optional, Union
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    Decorator to store history of inputs &
    outputs for a particular func in Redis

    Args:
        method : method to be decorated

    Returns:
        Callable: the decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        a wrapper function
        """
        key = method.__qualname__

        inputs_key = key + ":inputs"
        outputs_key = key + ":outputs"

        input_str = str(args)
        self._redis.rpush(inputs_key, input_str)

        output = method(self, *args, **kwargs)

        self._redis.rpush(outputs_key, str(output))

        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    decorator for counting times the class cache is called

    Args:
        method: the method to decorate

    Returns:
        Callable: the decorated method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        The wrapper function
        """
        key = method.__qualname__

        count = self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


def replay(method: Callable):
    """
    Display history of calls of particular function

    Args:
        method : method for which history is displayed
    """
    key = method.__qualname__

    inputs_key = key + ":inputs"
    outputs_key = key + ":outputs"

    inputs = cache._redis.lrange(inputs_key, 0, -1)
    outputs = cache._redis.lrange(outputs_key, 0, -1)

    print(f"{key} was called {len(inputs)} times:")

    for input_str, output_str in zip(inputs, outputs):
        input_args = eval(input_str)
        output = eval(output_str)

        print(f"{key}(*{input_args}) -> {output}")


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

    @count_calls
    @call_history
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
