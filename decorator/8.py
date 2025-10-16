def decorator(func:callable):

    def wrapper(*args, **kwargs):
        for arg in args:
            print(type(arg))
        for val in kwargs.values():
            print(type(val))
        return func(*args, **kwargs)

    return wrapper



@decorator
def myfunc(*n, **k):
    return n


myfunc(5, "2", a = 6)