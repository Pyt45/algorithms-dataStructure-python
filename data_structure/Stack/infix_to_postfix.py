from __future__ import annotations
from typing import Dict, Generic, TypeVar

def prec(c: str) -> int:
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    return -1

def infix_to_postfix(expression: str) -> str:
    postfix: str = ''
    s: list[str] = []

    for i in expression:
        if i == ' ':
            continue
        if (i <= 'z' and i >= 'a') or (i <= 'Z' and i >= 'A'):
            postfix += i
        elif i == '(':
            s.append(i)
        elif i == ')':
            while len(s) and s[-1] != '(':
                postfix += s[-1]
                del s[-1]
            if len(s):
                del s[-1]
        else:
            while len(s) and prec(i) <= prec(s[-1]):
                postfix += s[-1]
                del s[-1]
            s.append(i)
    
    while len(s):
        postfix += s[-1]
        del s[-1]
    
    return postfix

if __name__ == '__main__':
    print(infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))