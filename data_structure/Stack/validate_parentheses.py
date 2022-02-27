from __future__ import annotations
from typing import Dict

def validate_parentheses(expression: str) -> bool:
    pairs: Dict[str, str] = { '(': ')', '[': ']', '{': '}' }
    s: list[str] = []
    
    pass