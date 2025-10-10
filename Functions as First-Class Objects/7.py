from collections.abc import Callable

lst = [1, 2, 3]

def apply(func: Callable, nums: list[int]):
    l = []
    for i in range(len(nums)):
        l.append(func(nums[i]))

    return l

nums = [1, 2, 3, 4]
squares = apply(lambda x: x * x, nums)

print(squares)
print(nums)