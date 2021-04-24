from src.auction.bid import Bid

class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []

    def place_bid(self, bid: Bid):
        self.__bids.append(bid)

    @property
    def bids(self):
        # return a shallow copy of __bids
        return self.__bids[:]
