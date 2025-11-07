from db import Database
from Talaba import Student



class Manager:
    def __init__(self, ism, fam):
        self.ism = ism
        self.fam = fam
        self.__database = Database()

    def add_stuent(self, student):
        self.__database.append2file(repr(student))

    def get_students(self):
        all_data = self.__database.read_from_ile()
        students = []

        for data in all_data:
            data = data.replace('\n', '')
            id, ism, fam, grade = data.split("#")
            student = Student(id, ism, fam)
            student.set_grade(grade)
            students.append(student)

        return students

    def set_grade(self, id, grade):
        students = self.get_students()

        get_grade = False
        for student in students:
            if student.id == id:
                get_grade = True
                student.set_grade(grade)

        self.__database.write2file(students)

        return get_grade

    def del_student(self, id):
        students = self.get_students()

        is_del = False
        for i in range(len(students)):
            if students[i].id == id:
                students.pop(i)
                self.__database.write2file(students)
                is_del = True
                break

        return is_del
