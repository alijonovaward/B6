def choose(condition):
    if condition:
        return lambda x: x + 10
    else:
        return lambda x: x - 10


func = choose(False)

print(func(5))