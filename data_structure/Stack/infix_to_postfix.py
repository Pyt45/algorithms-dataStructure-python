from __future__ import annotations
from typing import Dict, Generic, TypeVar

def infix_to_postfix(expression: str, sep: bool = False):
    postfix: list[str] = []
    s: list[str] = []