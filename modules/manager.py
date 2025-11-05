class Manager:
    def __init__(self, ism, fam):
        self.ism = ism
        self.fam = fam
        self.__students = []

    def add_stuent(self, student):
        self.__students.append(student)

    def get_students(self):
        return self.__students

    def set_grade(self, id, grade):
        get_grade = False
        for student in self.__students:
            if student.id == id:
                get_grade = True
                student.set_grade(grade)

        return get_grade

    def del_student(self, id):
        is_del = False
        for i in range(len(self.__students)):
            if self.__students[i].id == id:
                self.__students.pop(i)
                is_del = True
                break

        return is_del
