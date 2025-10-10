def make_multiplier(n: int):
    return lambda x: x * n


func = make_multiplier(3)

print(func(3))