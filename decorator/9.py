def decorator(func:callable):

    def wrapper(*args, **kwargs):
        ans = func(*args, **kwargs)
        print(ans)
        print(ans)
        print(ans)

        return func(*args, **kwargs)

    return wrapper



@decorator
def myfunc(*n, **k):
    return n


myfunc(5, "2", a = 6)