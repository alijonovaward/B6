class Person:
    def __init__(self, name, surname, birthday, jshshir):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.jshshir = jshshir

    def __str__(self):
        return f"{self.name} {self.surname} - {self.birthday} - {self.jshshir}"


class Teacher(Person):
    def teaching(self):
        print("Teacher speaking...")

class Student(Person):
    def teach(self):
        print("Student learning...")

azamjon = Teacher("A'zamjon", "Alijonov", 30, 11)
mirodil = Student("Mirodil", "Barakayev", 13, 12)

azamjon.teaching()
print(azamjon)

mirodil.teach()
print(mirodil)