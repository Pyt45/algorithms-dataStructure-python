from __future__ import annotations
from typing import Dict

operand: Dict[str, function] = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '^': lambda x, y: x ** y,
}

def eval_expression(expression: str, sep: bool = False):
    s = []
    expr = expression.split() if sep is True else expression
    for i in expr:
        if i.isdigit() is True:
            s.append(i)
        elif i in ['+', '-', '/', '*', '^']:
            s.append(operand[i](int(s.pop()), int(s.pop())))
    return s[-1]

if __name__ == '__main__':
    print(eval_expression("456*+"))
    print(eval_expression("32^5*32*3-/5+"))
    print(eval_expression("1234^5-678*+^*+9-"))
    print(eval_expression("12345*+*+"))