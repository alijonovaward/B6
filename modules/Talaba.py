class Student:
    def __init__(self, id, ism, fam):
        self.id = id
        self.ism = ism
        self.fam = fam
        self.__grade = 0

    def __str__(self):
        return f"{self.ism} {self.fam} {self.__grade}"

    def set_grade(self, grade):
        self.__grade = grade