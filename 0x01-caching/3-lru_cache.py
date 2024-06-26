#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and implements
    a caching system with an LRU (Least Recently Used) eviction policy.
    """

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the maximum limit, discard the least recently used item.
        Args:
            key (str): The key for the item.
            item (any): The item to cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

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
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
