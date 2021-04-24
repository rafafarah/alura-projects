import sys
from auction import Auction

class Inspector:
    def __init__(self):
        self.higher_bid = sys.float_info.min
        self.lower_bid = sys.float_info.max

    # annotation: parameter auction expect
    # an object of calss Auction
    # it's possible to overwrite it with other type
    def inspect(self, auction:Auction):
        for bid in auction.bids:
            if bid.value > self.higher_bid:
                self.higher_bid = bid.value
            if bid.value < self.lower_bid:
                self.lower_bid = bid.value
