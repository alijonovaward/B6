def call_logger(func:callable):
    history = []

    def wrapper(*args, **kwargs):
        nonlocal history
        try:
            res = func(*args, **kwargs)
        except Exception as e:
            res = e

        history.append(
            {
                "args": args,
                "kwargs": kwargs,
                "res": res
            }
        )
        return res

    def get_history():
        nonlocal history
        return history

    wrapper.history = get_history

    return wrapper

@call_logger
def add(a, b):
    return a + b

@call_logger
def div(a, b):
    return a / b


print(add(2, 3))
print(add(3, 7))
print(add.history())


print("#######################")

print(div(5, 10))
print(div(10, 0))
print(div.history())


