from __future__ import annotations

def binary_search(l: list, target: int, high: int) -> int | None:
    left: int = 0
    right: int = high - 1
    while left <= right:
        mid = left + (right - left) // 2
        if l[mid] == target:
            return mid
        elif target > l[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None


if __name__ == '__main__':
    l = [3, 4, 8, 9, 14, 34, 41, 49, 58, 65, 69, 77, 81, 85, 88]
    print(binary_search(l, 3, len(l)))
    print(binary_search(l, 41, len(l)))
    print(binary_search(l, 88, len(l)))
    print(binary_search(l, 89, len(l)))