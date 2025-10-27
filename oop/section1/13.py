class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_from_point(self, x1, y1):
        return ((self.x - x1) ** 2 + (self.y - y1) ** 2) ** 0.5


p = Point(3, 4)
print(p.distance_from_origin())

print(p.distance_from_point(10, 13))