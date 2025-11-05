class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    @classmethod
    def get_from_dict(cls, d):
        name = d.get('name', "Berilmagan")
        age = d.get('age', 0)
        return cls(name, age)



p = Person("Javohir", 11)
fp = Person.get_from_dict({"ism":"eshmat", "age": 11})
print(fp)