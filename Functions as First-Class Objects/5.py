from typing import Callable

def apply(func:callable,val:int):
    return func(val)

print(apply(lambda x: x*x,5))