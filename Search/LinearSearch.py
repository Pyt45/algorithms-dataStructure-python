from __future__ import annotations

def linear_search(l: list, target: int) -> int | None:
    for i in range(len(l)):
        if target == l[i]:
            return i
    return None


if __name__ == '__main__':
    l = [41, 4, 3, 88, 34, 8, 85, 69, 49, 58, 65, 81, 9, 77, 14]
    print(linear_search(l, 41)) # best case finding the element at index 0
    print(linear_search(l, 14)) # worst case finding element at the final index
    print(linear_search(l, 69))