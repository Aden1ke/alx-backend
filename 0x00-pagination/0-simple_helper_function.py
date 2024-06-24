#!/usr/bin/env python3
"""
This module contains a helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for the given page and page size.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size  # Calculate the start position
    end_index = page * page_size  # Calculate the end position
    return start_index, end_index  # Return the positions as a tuple
