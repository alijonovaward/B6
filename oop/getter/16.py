class Temperature:
    def __init__(self, degree):
        self._celsius = degree

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, degree):
        if degree > -273.15:
            self._celsius = degree

    @celsius.deleter
    def celsius(self):
        print("deleting celsius...")
        del self._celsius

t = Temperature(10)
t.set_celsius = -100
del t.celsius
