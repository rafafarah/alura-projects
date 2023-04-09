
class AudioVisual:
    def __init__(self, name, year):
        self._name = name.title()
        self._year = year
        self._likes = 0

    def like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @property
    def year(self):
        return self._year

    @property
    def likes(self):
        return self._likes

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @year.setter
    def year(self, new_year):
        self._year = new_year

    def __str__(self):
        return f'{self._name} - {self.year} - {self.likes} likes'
