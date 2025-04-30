#!/usr/bin/env python3
"""Hypermedia pagination module"""


import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """Calculates the start and end index for pagination"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


# Reprise du code de l'exercice 0 et 1
class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return page of dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_idx:end_idx]

        # Novelle fonction pour la pagination hypermédia
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary with pagination metadata."""
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
