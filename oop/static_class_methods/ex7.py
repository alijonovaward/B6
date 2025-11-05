class Are:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def random_color(cls, val):
        return cls(val, val)
    def get_area(self):
        return self.x * self.y


my_color = Are(6, 5)
ran = Are.random_color(6)

print(my_color)
print(ran.get_area())