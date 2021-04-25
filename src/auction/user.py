from src.auction.bid import Bid

class User:

    def __init__(self, name, wallet=0):
        self.__name = name
        self.__wallet = wallet

    def place_bid(self, auction, value):
        bid = Bid(self, value)
        auction.place_bid(bid)
        self.__wallet -= value

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__wallet
