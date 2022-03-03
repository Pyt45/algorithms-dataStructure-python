from __future__ import annotations
from random import sample

# def merge(l: list, left: int, mid: int, right: int) -> list:
    # """ Merge the tow sorted list l[left:mid] [mid + 1:right] """
    # print(left, mid, right)
    # if l[left:mid] > l[mid:right]:
    #     return l[left:mid] + l[mid:right]
    # return l[mid:right] + l[left:mid]

def merge_sort(l: list) -> list | None:
    # if left > right:
    #     return
    # mid = left + (right - left) // 2
    # merge_sort(l, left, mid)
    # merge_sort(l, mid + 1, right)
    # return merge(l, left, mid, right)
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if right[j] < left[i]:
                l[k] = right[j]
                j += 1
            else:
                l[k] = left[i]
                i += 1
            k += 1
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
        


if __name__ == '__main__':
    l = sample(range(0, 100), 15)
    print(l)
    merge_sort(l)
    print(l)