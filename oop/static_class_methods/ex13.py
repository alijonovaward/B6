class Person:
    def check_email(email:str):
        if "@" in email:
            return True
        return False


print(Person.check_email("Alijonovrobogmail.com"))