from typing import Callable

def apply(func:callable,val1:int, val2: int):
    return func(val1, val2)

print(apply(lambda x, y: x - y,5, 10))