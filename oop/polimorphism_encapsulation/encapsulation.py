class Person:
    def __init__(self, name, surname, birthday, jshshir):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.__jshshir = jshshir

    def __str__(self):
        return f"{self.name} {self.surname} - {self.birthday} - {self.jshshir}"