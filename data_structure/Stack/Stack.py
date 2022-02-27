#!/usr/bin/env python3

from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar('T')

class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass

class Stack(Generic[T]):
    def __init__(self, cap: int = 0) -> None:
        self.items: list[T] = []
        self.cap: int = cap
        self.index: int = 0
    def __str__(self) -> str:
        return str(self.items)
    def push(self, item) -> None:
        """insert item on top of stack"""
        if self.index < self.cap:
            self.items.append(item)
            self.index += 1
        else:
            raise StackOverflowError

    def pop(self) -> T:
        """delete the topmost item and return it"""
        if self.index == 0:
            raise StackUnderflowError
        poped = self.items[self.index - 1]
        del self.items[self.index - 1]
        self.index -= 1
        return poped

    def top(self) -> T:
        """return the top item of the stack"""
        if self.index == 0:
            raise StackUnderflowError
        return self.items[self.index - 1]

    def is_empty(self) -> bool:
        """check if stack is empty"""
        return self.index == 0

    def is_full(self) -> bool:
        """check if stack is full"""
        return self.cap == self.index

    def size(self) -> int:
        """Return the size of stack"""
        return len(self.items)

    def __contains__(self, item: T) -> bool:
        """check if item in stack"""
        return item in self.items

if __name__ == '__main__':
    s = Stack[int](5)

    assert s.size() == 0
    try:
        _ = s.pop()
        assert False # this should not happen
    except StackUnderflowError as e:
        assert True # this should happen

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    assert str(s) == str([1, 2, 3, 4, 5])
    try:
        s.push(6)
        assert False # this should not happen
    except StackOverflowError as e:
        assert True # this should happen

    assert s.pop() == 5
    assert s.top() == 4
    assert 2 in s
    assert s.is_empty() is False
    assert s.is_full() is False
