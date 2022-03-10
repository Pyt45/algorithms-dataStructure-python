from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")

class QueueOverflowError(BaseException):
    pass

class QueueUnderflowError(BaseException):
    pass

class Queue(Generic[T]):
    def __init__(self, limit: int = 0) -> None:
        self.queue: list[T] = []
        self.limit: int = limit
        self.index: int = 0

    def __str__(self) -> str:
        return f"{self.queue}"
    
    def __contains__(self, item) -> bool:
        """check if item in queue"""
        return item in self.queue
    
    def is_empty(self) -> bool:
        return self.index == 0

    def is_full(self) -> bool:
        return self.index == self.limit
    
    def size(self) -> int:
        return self.index

    def peek(self) -> T:
        """return the item at the top of the queue"""
        if self.index == 0:
            raise QueueUnderflowError
        return self.queue[self.index - 1]

    def enqueue(self, item: int) -> T:
        """insert an item to the end of the queue"""
        if self.index >= self.limit:
            raise QueueOverflowError
        self.index += 1
        self.queue.append(item)

    def dequeue(self) -> T:
        """delete an item from the beginning of the queue"""
        if self.index == 0:
            raise QueueUnderflowError
        self.index -= 1
        return self.queue.pop(0)

if __name__ == '__main__':
    q = Queue[int](5)
    print(q.size())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(f"queue: {str(q)}")
    print(f"size = {q.size()}")

    print(f"last: {q.peek()}")
    print(f"poped: {q.dequeue()}")
    print(f"queue: {str(q)}")
    print(f"size = {q.size()}")