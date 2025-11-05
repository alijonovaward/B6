class DEVICE:
    def __init__(self,nomi:str):
        self.nomi=nomi
    def status(self):
        return f" qurilma nomi:{self.nomi}"
class Phone(DEVICE):
    def status(self):
        return f"telefon nomi:{self.nomi}"
class Laptop(DEVICE):
    def status(self):
        return f"kompyuter nomi:{self.nomi}"
p1=Phone("Redmi")
l1=Laptop("Lenova")
print(p1.status())
print(l1.status())