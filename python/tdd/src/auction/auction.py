from src.auction.bid import Bid
from src.auction.exceptions import InvalidBid

class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.highest_bid = 0.0
        self.lowest_bid = 0.0

    def place_bid(self, bid: Bid):
        if self._is_bid_valid(bid):
            # update lowest_bid and highest_bid
            if not self._has_bids():
                self.lowest_bid = bid.value
            self.highest_bid = bid.value

            self.__bids.append(bid)
        else:
            raise InvalidBid('User cannot place two bids in a row, neither place a smaller than last bid')

    @property
    def bids(self):
        # return a shallow copy of __bids
        return self.__bids[:]

    def _has_bids(self):
        return self.__bids

    def _is_current_user_different_than_last_user(self, bid):
        return self.__bids[len(self.__bids) - 1].user != bid.user

    def _is_value_greater_than_previous_bid(self, bid):
        # self.__bids[-1] is equivalent to self.__bids[len(self.__bids) - 1]
        return self.__bids[-1].value < bid.value

    def _is_bid_valid(self, bid):
        # place bid if list is either empty or if last user is different from current user and current bid is greater than previous bid
        return not self._has_bids() or (self._is_current_user_different_than_last_user(bid)
            and self._is_value_greater_than_previous_bid(bid))
