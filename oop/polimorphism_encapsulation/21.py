class Flyer:
    def __init__(self, high):
        self.high = high
    def speak(self):
        print("f speak")

    def fly(self):
        print("flying...")

class Swimmer:
    def __init__(self, depth):
        self.depth = depth

    def swim(self):
        print("swimming...")

    def speak(self):
        print("uuuuuuvbfcnvbgfhbnu")

class Duck(Flyer, Swimmer):
    def __init__(self, high, depth):
        Flyer.__init__(self, high)
        Swimmer.__init__(self, depth)
    def speak(self):
        Swimmer.speak(self)

d = Duck(100, 10)
d.fly()
d.swim()
d.speak()