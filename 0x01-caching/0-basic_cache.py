#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching and implements
    a basic caching system with no limit on items.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key for the item.
            item (any): The item to cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key (str): The key for the item.

        Returns:
            The item if found, None otherwise.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
