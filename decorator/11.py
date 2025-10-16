def decorator(func:callable):

    def wrapper(*args):
        evens = []
        for arg in args:
            if arg % 2 == 0:
                evens.append(arg)

        func(*tuple(evens))

    return wrapper



@decorator
def myfunc(*n):
    print(n)


myfunc(5, 5, 3, 4, 6, 7, 9)