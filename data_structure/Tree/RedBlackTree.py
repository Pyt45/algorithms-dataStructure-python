from __future__ import annotations
from typing import Generic, TypeVar, Dict

K = TypeVar('K')
V = TypeVar('V')
pair = TypeVar('Pair')


class Pair(Generic[K, V]):

    def __init__(self, first, second) -> None:
        self.first: K = first
        self.second: V = second
    
    def __str__(self) -> str:
        return f"first: {self.first}, second: {self.second}"


class Node(Generic[pair]):
    pass

class RedBlackTree():
    pass

if __name__ == '__main__':
    p = Pair[int, int](1, 3)
    print(p)
