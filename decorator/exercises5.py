def conditional(cond:callable):
    def decorator(func:callable):
        def wrapper(*args, **kwargs):
            if cond(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                print("Skipped due to condition.")

        return wrapper

    return decorator

@conditional(lambda x, y: x > y)
def add(a, b):
    print(a, b)


add(10, 20)