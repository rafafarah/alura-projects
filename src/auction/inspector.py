import sys
from src.auction.auction import Auction

class Inspector:
    def __init__(self):
        self.highest_bid = sys.float_info.min
        self.lowest_bid = sys.float_info.max

    # annotation: parameter auction expect
    # an object of calss Auction
    # it's possible to overwrite it with other type
    def inspect(self, auction:Auction):
        for bid in auction.bids:
            if bid.value > self.highest_bid:
                self.highest_bid = bid.value
            if bid.value < self.lowest_bid:
                self.lowest_bid = bid.value
