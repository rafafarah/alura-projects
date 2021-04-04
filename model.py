class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.__year = year
        self.__duration = duration
        self.__likes = 0

    def like(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @property
    def duration(self):
        return self.__duration

    @property
    def likes(self):
        return self.__likes

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @duration.setter
    def duration(self, new_duration):
        self.__duration = new_duration




class Serie:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.__year = year
        self.__seasons = seasons
        self.__likes = 0

    def like(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @property
    def seasons(self):
        return self.__seasons

    @property
    def likes(self):
        return self.__likes

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @seasons.setter
    def seasons(self, new_seasons):
        self.__seasons = new_seasons

