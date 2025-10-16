def decorator(func:callable):

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res is None:
            return "no result!"
        return res
    return wrapper



@decorator
def myfunc(*n, **k):

    return


print(myfunc(5, "2", a = 6))