def decorator(func:callable):

    def wrapper(*args):
        evens = []
        for arg in args:
            if isinstance(arg, str):
                evens.append(arg.lower())
            else:
                evens.append(arg)

        func(*tuple(evens))

    return wrapper



@decorator
def myfunc(*n):
    print(n)


myfunc(5, 5, 3, 4, 6, 7, 9, "azaMjon", "Jasur")