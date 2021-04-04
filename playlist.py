
class Playlist:
    def __init__(self, name, shows):
        self._name = name
        self._shows = shows
    
    @property
    def shows(self):
        return self._shows
    
    @property
    def len(self):
        return len(self._shows)
