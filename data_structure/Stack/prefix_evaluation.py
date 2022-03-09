from __future__ import annotations
from ast import Dict

operand: Dict[str, function] = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '^': lambda x, y: x ^ y,
}

def eval_expression(expression: str, sep: bool = False):
    s = []
    exprs = expression.split()[::-1] if sep is True else expression[::-1]
    for i in exprs:
        if i.isdigit() is True:
            s.append(i)
        elif i in ['+', '-', '/', '*', '^']:
            s.append(operand[i](int(s.pop()), int(s.pop())))
    return s[-1]

if __name__ == '__main__':
    print(eval_expression("/ * 10 2 + 4 1", sep=True))
    print(eval_expression("+9*26"))