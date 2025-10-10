lambdas = [
    lambda x: x,
    lambda x: 2 * x,
    lambda x: 3 * x,
    lambda x: 4 * x,
    lambda x: 5 * x
]

for i in lambdas:
    print(i(10))