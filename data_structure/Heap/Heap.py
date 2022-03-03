from __future__ import annotations
from typing import Generic, TypeVar, Iterable

T = TypeVar("T")

class Heap(Generic[T]):
    """max heap implementation"""
    def __init__(self) -> None:
        self.heap: list[T] = []

    def __repr__(self) -> str:
        return str(self.heap)

    def parent_index(self, index: int) -> int | None:
        if index > 0 and index < len(self.heap):
            return (index - 1) // 2
        return None
    
    def left_index(self, index: int) -> int | None:
        left = 2 * index + 1
        if left >= len(self.heap):
            return None
        return left
    
    def right_index(self, index: int) -> int | None:
        right = 2 * index + 2
        if right >= len(self.heap):
            return None
        return right
    
    def maximum(self) -> T | None:
        return self.heap[0] if len(self.heap) > 0 else None
    
    def max_heapify(self, index: int) -> None:
        if index < len(self.heap):
            left, right = self.left_index(index), self.right_index(index)
            mx = left if left is not None and self.heap[left] > self.heap[index] else index
            mx = right if right is not None and self.heap[right] > self.heap[mx] else mx
            if mx != index:
                self.heap[mx], self.heap[index] = self.heap[index], self.heap[mx]
                self.max_heapify(mx)
    
    def build_max_heap(self, collection: Iterable[T]) -> None:
        """build max heap from an unsorted array"""
        # 17, 3, 4, 5, 6, 7
        self.heap = list(collection)
        for i in range((len(self.heap) - 1) // 2, -1, -1):
            self.max_heapify(i)

    def extract_max(self) -> T:
        """get and remove max from heap"""
        item = self.maximum()
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.max_heapify(0)
        return item

    def insert(self, item: T) -> None:
        self.heap.append(item)
        index = (len(self.heap) - 1) // 2
        while index >= 0:
            self.max_heapify(index)
            index = (index - 1) // 2

if __name__ == '__main__':
    # h = Heap[int]()
    # h.insert(17)
    # h.insert(6)
    # h.insert(5)
    # h.insert(2)
    # h.insert(4)
    # h.insert(13)
    # h.insert(1)
    # print(h)
    for unsorted in [
        [0],
        [2],
        [3, 5],
        [5, 3],
        [5, 5],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 2, 3, 5],
        [0, 2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [-45, -2, -5],
    ]:
        print(f"unsorted array: {unsorted}")

        heap = Heap()
        heap.build_max_heap(unsorted)
        print(f"after build heap: {heap}")