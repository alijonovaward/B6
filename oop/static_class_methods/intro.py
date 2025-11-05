class A:
    def __init__(self, a):
        self.a = a
        print("A class constructor")

class B:
    def __init__(self, b):
        self.b = b
        print("B class constructor")

class C(A, B):
    def __init__(self, a, b):
        A.__init__(self, a)   # A ning konstruktorini chaqiramiz
        B.__init__(self, b)   # B ning konstruktorini chaqiramiz
        print("C class constructor")

