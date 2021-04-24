class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []

    @property
    def bids(self):
        return self.__bids
