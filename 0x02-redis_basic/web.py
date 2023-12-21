#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
import redis
from functools import wraps
from typing import Callable


redis_store = redis.Redis()


def data_cache(method: Callable) -> Callable:
    """
    Caches output of fetched data $ counts access

    Args:
        method (Callable): function to decorate

    Returns:
        Callable: decorated function
    """
    @wraps(method)
    def wrapper(url) -> str:
        """
        Wrapper function

        Args:
        url (str): URL for which data is fetched

        Returns:
            str: content of the URL
        """
        # Increment the access count
        redis_store.incr(f'count:{url}')

        # Check if the result is already cached
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        # If not, fetch the page content
        result = method(url)

        # Reset the access count and cache the result with expiration
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)

        return result
    return wrapper


@data_cache
def get_page(url: str) -> str:
    """
    Returns content of URL after caching request's response
    & tracking request

    Args:
        url (str): URL which is data fetched

    Returns:
        str: content of the URL.
    """
    return requests.get(url).text


# Example usage
url = "http://slowwly.robertomurray.co.uk"
content = get_page(url)
print(content)

# accessing the same URL again
content_cached = get_page(url)
print(content_cached)