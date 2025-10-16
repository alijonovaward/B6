# from typing import Callable
#
# def decorator(func:Callable):
#     def wrapper():
#         print(func.__name__)
#         func()
#
#     return wrapper
#
# @decorator
# def countDown():
#     for i in range(2, 0, -1):
#         print(i)
#
# countDown()
# countDown()


from typing import Callable

def decorator(func: Callable):
    def wrapper(string):
        res = func(string)
        return res.upper()

    return wrapper

@decorator
def myfunc(n):
    return f"{n}"

print(myfunc("Hello Javohir"))