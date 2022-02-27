from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")

class BinaryHeap(Generic[T]):
    parent: function = lambda n: (n - 1) / 2
    left: function = lambda n: 2 * n + 1
    right: function = lambda n: 2 * n + 2
    def __init__(self):
        self.heap: list[T] = []
    
    def insert(self, item):

        return

if __name__ == '__main__':
    pass