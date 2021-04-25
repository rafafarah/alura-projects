import sys
from src.auction.bid import Bid

class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.highest_bid = sys.float_info.min
        self.lowest_bid = sys.float_info.max

    def place_bid(self, bid: Bid):
        # self.__bids[-1] is equivalent to self.__bids[len(self.__bids) - 1]
        # place bid if list is either empty or if last user is different from current user
        if (not self.__bids or
            self.__bids[len(self.__bids) - 1].user != bid.user and
            self.__bids[-1].value < bid.value):
            if bid.value > self.highest_bid:
                self.highest_bid = bid.value
            if bid.value < self.lowest_bid:
                self.lowest_bid = bid.value

            self.__bids.append(bid)
        else:
            raise ValueError('User cannot place two bids in a row, neither place a smaller than last bid')

    @property
    def bids(self):
        # return a shallow copy of __bids
        return self.__bids[:]
