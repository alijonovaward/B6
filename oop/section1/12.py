class Player:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def add_score(self, points):
        self.score += points

player = Player("Football", 10)
player.add_score(10)
print(player.score)