class Person:
    def __init__(self, name, surname, birthday, jshshir):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.jshshir = jshshir

    def speak(self):
        print("Waiting implement")

    def __str__(self):
        return f"{self.name} {self.surname} - {self.birthday} - {self.jshshir}"


class English(Person):
    def speak(self):
        print("I'm speak in English")

class French(Person):
    def speak(self):
        print("I'm speak in French")

azamjon = English("A'zamjon", "Alijonov", 30, 11)
mirodil = French("Mirodil", "Barakayev", 13, 12)

azamjon.speak()
mirodil.speak()
