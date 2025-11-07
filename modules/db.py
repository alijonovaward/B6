class Database:
    def __init__(self, directory = "data.txt"):
        self.directory = directory

    def write2file(self, datas):
        with open(self.directory, "w") as file:
            file.write("")

        for data in datas:
            self.append2file(repr(data))


    def append2file(self, data):
        with open(self.directory, "a") as file:
            file.write(data + "\n")

    def read_from_ile(self):
        with open(self.directory, "r") as file:
            all_lines = file.readlines()

        return all_lines

# db = Database()
# print(db.read_from_ile())
