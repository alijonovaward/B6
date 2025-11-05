class A:
    def __init__(self):
        print("A initializing")

class B:
    def __init__(self):
        print("B initializing")

class C(B, A):
    def __init__(self):
        B.__init__(self)
        A.__init__(self)

c = C()