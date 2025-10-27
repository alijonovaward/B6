class Movie:
    def __init__(self, title: str, year: int, genre: str):
        self.title = title
        self.year = year
        self.genre = genre

    def info(self):
        return f"{self.title}, {self.genre}, {self.year}"

avengers = Movie("Qasoskorlar 1", 2010, "fantastik")

print(avengers.info())