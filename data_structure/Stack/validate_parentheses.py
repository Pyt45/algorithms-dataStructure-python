from __future__ import annotations
from typing import Dict

def validate_parentheses(expression: str) -> bool:
    pairs: Dict[str, str] = { '(': ')', '[': ']', '{': '}' }
    s: list[str] = []
    for i in range(len(expression)):
        s.append(expression[i])
        if len(s) >= 2 and pairs.get(s[-2]) == s[-1]:
            s.pop()
            s.pop()
    return len(s) == 0

if __name__ == '__main__':
    print(validate_parentheses("[]{}({[]}){"))
    print(validate_parentheses("["))
    print(validate_parentheses("[]{}({[]})"))
    print(validate_parentheses("[{(())}]"))