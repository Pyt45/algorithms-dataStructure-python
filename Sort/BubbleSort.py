from __future__ import annotations
from random import sample

def bubble_sort(l: list):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[j] < l[i]:
                print(f"before swap --> r: {j}:{l[j]}, l: {i}:{l[i]}")
                l[j], l[i] = l[i], l[j]
                # print(f"after swap --> r: {l[j]}, l: {l[i]}")

if __name__ == '__main__':
    l = sample(range(0, 100), 4)
    print(l)
    bubble_sort(l)
    print(l)