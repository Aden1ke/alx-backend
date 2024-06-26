#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements
    a caching system with a LIFO (Last In First Out) eviction policy.
    """

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the maximum limit,
        Args:
            key (str): The key for the item.
            item (any): The item to cache.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= self.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        if key in self.cache_data:
            self.stack.remove(key)
        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key from the cache.
        Args:
            key (str): The key for the item.
        Returns:
            any: The item linked to the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
