from audiovisual import AudioVisual

class Movie(AudioVisual):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        self._duration = new_duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self._duration} min - {self.likes} likes'