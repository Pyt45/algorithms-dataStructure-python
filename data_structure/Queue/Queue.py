from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self, limit: int = 0) -> None:
        self.items = []
        self.limit = limit
        self.index = 0

    def __str__(self) -> str:
        return f"{self.items}"
    
    def __contains__(self, item) -> bool:
        """check if item in queue"""
        return item in self.items
    
    def is_empty(self) -> bool:
        pass
    
    def size(self) -> int:
        pass

    def peek(self) -> T:
        """return the item at the top of the queue"""
        pass

    def enqueue(self, item) -> T:
        """insert an item to the end of the queue"""
        pass

    def dequeue(self, item) -> T:
        """delete an item from the beginning of the queue"""
        pass

if __name__ == '__main__':
    q = Queue(5)