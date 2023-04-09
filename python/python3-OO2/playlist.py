
class Playlist:
    def __init__(self, name, shows):
        self._name = name
        self._shows = shows

    def __getitem__(self, item):
        return self._shows[item]

    def __len__(self):
        return len(self._shows)
