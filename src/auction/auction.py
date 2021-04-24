import sys
from src.auction.bid import Bid

class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.highest_bid = sys.float_info.min
        self.lowest_bid = sys.float_info.max

    def place_bid(self, bid: Bid):
        if bid.value > self.highest_bid:
            self.highest_bid = bid.value
        if bid.value < self.lowest_bid:
            self.lowest_bid = bid.value

        self.__bids.append(bid)

    @property
    def bids(self):
        # return a shallow copy of __bids
        return self.__bids[:]
