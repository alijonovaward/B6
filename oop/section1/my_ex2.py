class Battery:
    def __init__(self, percentage):
        self.history = []
        self.percentage = percentage
        if percentage > 100:
            self.percentage = 100
        elif percentage < 0:
            self.percentage = 0
        self.history.append(f"{self.percentage} boshidagi zaryad")

    def charger(self, time: int, num: int):
        if num < 0:
            return
        self.percentage += time * num
        self.percentage = min(100, self.percentage)
        self.history.append(f"{time} minut -> {num}% dan zaryadlandi")

    def play(self, time: int, num: int):
        self.percentage -= time * num
        self.percentage = max(0, self.percentage)
        self.history.append(f"{time} minut -> {num}% dan o'ynaldi")

b = Battery(60)
b.charger(10, 5)
b.play(10, 3)
b.charger(6, 5)
print(b.percentage)
print(b.history)