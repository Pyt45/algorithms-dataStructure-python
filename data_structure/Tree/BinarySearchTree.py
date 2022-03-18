from __future__ import annotations
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")

class Pair(Generic[K, V]):
    def __init__(self, first: K, second: V) -> None:
        self.first: K = first
        self.second: V = second

class Node(Generic[K, V]):
    def __init__(self, pair: Pair[K, V]) -> None:
        self.pair = pair
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree(Generic[K, V]):
    def __init__(self) -> None:
        self.root = None
        self.start = None
        self.end = None
    
    def __iadd__(self, __o: int) -> object: # B += 1
        pass
    def __lt__(self, __o: object) -> bool:
        pass
    def __le__(self, __o: object) -> bool:
        pass
    def __eq__(self, __o: object) -> bool:
        pass
    def __ne__(self, __o: object) -> bool:
        pass
    def __gt__(self, __o: object) -> bool:
        pass
    def __ge__(self, __o: object) -> bool:
        pass
    
    def insert(self, node: Node[K, V]):
        pass
    def remove(self, node: Node[K, V]):
        pass
    def clear(self):
        pass
