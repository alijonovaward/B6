def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

d = {
    "add": add,
    "sub": subtract,
    "mul": mul
}

a = int(input("a = "))
b = int(input("b = "))
amal = input("Tanlang ['add', 'sub', 'mul'] = ")

print(d[amal](a, b))