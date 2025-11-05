class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def newborn(cls, name):
        return cls(name, 0)

    def __str__(self):
        return f"{self.name} - {self.age}"

p = Person("Javohir", 11)

baby = Person.newborn("Mustafo")

print(p)
print(baby)