from __future__ import annotations
from random import sample

def partition(l: list, left: int, right: int) -> int:
    pivot = l[right]
    i = left - 1
    j = left
    while j < right:
        if l[j] < pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
        j += 1
    l[i + 1], l[right] = l[right], l[i + 1]
    return i + 1

def quick_sort(l: list, left: int, right: int) -> None:
    """ left: starting index, right: ending index """
    if left < right:
        pivot = partition(l, left, right) # pivot index
        quick_sort(l, left, pivot - 1)
        quick_sort(l, pivot + 1, right)

if __name__ == '__main__':
    l = sample(range(0, 100), 16)
    print(l)
    quick_sort(l, 0, len(l) - 1)
    print(l)