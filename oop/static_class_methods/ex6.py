class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"

    @classmethod
    def random_color(cls):
        import random

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return cls(r, g, b)



my_color = Color(255, 255, 0)
ran = Color.random_color()

print(my_color)
print(ran)