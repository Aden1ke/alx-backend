#!/usr/bin/env python3
"""
FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and implements
    a caching system with a FIFO (First In First Out) eviction policy.
    """

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the maximum limit, discard the oldest item.
        Args:
            key (str): The key for the item.
            item (any): The item to cache.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        if key not in self.cache_data:
            self.order.append(key)
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
