from __future__ import annotations
from typing import Generic, TypeVar
from collections.abc import Iterator

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item: T = item
        self.next = None

class LinkedList(Generic[T]):
    def __init__(self, *args) -> None:
        self.head = None
    def __iter__(self) -> Iterator[T]:
        curr = self.head
        while curr is not None:
            yield curr.item
            curr = curr.next
    def __str__(self) -> str:
        return '->'.join([str(item) for item in self])
    # def __add__(self, count: int):
    #     return LinkedList()
    def append(self, item: T) -> None:
        """push item to the end of the linked_list"""
        if self.head is None:
            self.head = Node[T](item)
        else:
            curr = self.head
            while curr is not None and curr.next is not None:
                curr = curr.next
            new_node = Node[T](item)
            curr.next = new_node
    def remove(self) -> None:
        """remove item from the end of the linked_list """
        item = None
        if self.head is not None and self.head.next is None:
            item = self.head.item
            self.head = None
        else:
            curr = self.head
            prev = None
            while curr is not None and curr.next is not None:
                prev = curr
                curr = curr.next
            item = curr.item
            prev.next = curr.next
        return item
    def top(self):
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr.item if curr else None

class StackOverFlowError(Exception):
    pass

class StackUnderFlowError(Exception):
    pass

class Stack(Generic[T]):
    def __init__(self, cap: int = 0) -> None:
        self.stack: LinkedList[T] = LinkedList[T]()
        self.cap: int = cap
        self.index: int = 0
    def __str__(self):
        return str(self.stack)
    def push(self, item: T) -> None:
        """insert item on top of stack"""
        if self.index >= self.cap:
            raise StackOverFlowError
        self.stack.append(item)
        self.index += 1
    def pop(self) -> T:
        """delete the topmost item and return it"""
        if self.index == 0:
            raise StackUnderFlowError
        return self.stack.remove()
    def top(self) -> T:
        """return the top item of the stack"""
        return self.stack.top()
    def is_empty(self) -> bool:
        """check if stack is empty"""
        return self.index == 0
    def is_full(self) -> bool:
        """check if stack is full"""
        return self.cap == self.index
    def size(self) -> int:
        """Return the size of stack"""
        return self.index
    def __contains__(self, item: T) -> bool:
        """check if item in stack"""
        return item in self.stack

def Path(func: function):
    def inner_func(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return inner_func

@Path
def test():
    print("hello")

if __name__ == '__main__':
    test()
    s = Stack[int](5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    try:
        s.push(6)
        assert False # this should not happens
    except:
        assert True # this should happen
    print(str(s))
    print(s.is_empty())
    print(s.is_full())
    print(5 in s)
    print(s.size())
    print(s.top())
    print(s.pop())
    print(str(s))