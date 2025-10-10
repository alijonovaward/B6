def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operations = [add, subtract]

a = int(input("a = "))
b = int(input("b = "))

for o in operations:
    print(o(a, b))