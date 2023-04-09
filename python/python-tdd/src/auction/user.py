from src.auction.bid import Bid
from src.auction.exceptions import InvalidBid

class User:

    def __init__(self, name, wallet=0):
        self.__name = name
        self.__wallet = wallet

    def place_bid(self, auction, value):
        if self._is_value_valid(value):
            bid = Bid(self, value)
            auction.place_bid(bid)
            self.__wallet -= value
        else:
            raise InvalidBid('Bid value should be less than wallet')

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__wallet

    def _is_value_valid(self, value):
        return self.__wallet >= value
