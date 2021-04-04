from audiovisual import AudioVisual

class Serie(AudioVisual):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self._seasons = seasons

    @property
    def seasons(self):
        return self._seasons

    @seasons.setter
    def seasons(self, new_seasons):
        self._seasons = new_seasons
    
    def __str__(self):
        return f'{self._name} - {self.year} - {self._seasons} seasons - {self.likes} likes'