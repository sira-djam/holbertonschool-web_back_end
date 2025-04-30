#!/usr/bin/env python3

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
                         and the end index (exclusive) for slicing.
    """
    # Calculate the starting index of the page
    start_index = (page - 1) * page_size

    # Calculate the ending index (not inclusive)
    end_index = page * page_size

    # Return the tuple with start and end indexes
    return (start_index, end_index)

