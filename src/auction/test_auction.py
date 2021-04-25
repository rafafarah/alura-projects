from unittest import TestCase
from src.auction.user import User
from src.auction.bid import Bid
from src.auction.auction import Auction

class TestAuction(TestCase):
    # should run before every test case
    def setUp(self):
        self.jorge = User('Jorge')
        self.bid_jorge = Bid(self.jorge, 100)
        self.auction = Auction('Cellphone')

    def test_should_get_highest_and_lowest_bids_when_added_in_ascending_order(self):
        jeff = User('Jefferson')
        bid_jeff = Bid(jeff, 150)
        self.auction.place_bid(self.bid_jorge)
        self.auction.place_bid(bid_jeff)

        self.assertEqual(150, self.auction.highest_bid)
        self.assertEqual(100, self.auction.lowest_bid)

    def test_should_get_highest_and_lowest_bids_when_added_in_descending_order(self):
        jeff = User('Jefferson')
        bid_jeff = Bid(jeff, 150)
        self.auction.place_bid(bid_jeff)
        self.auction.place_bid(self.bid_jorge)

        self.assertEqual(150, self.auction.highest_bid)
        self.assertEqual(100, self.auction.lowest_bid)

    def test_should_get_same_value_for_highest_and_lowest_bids_when_auction_has_a_single_bid(self):
        self.auction.place_bid(self.bid_jorge)

        self.assertEqual(100, self.auction.highest_bid)
        self.assertEqual(100, self.auction.lowest_bid)

    def test_should_get_highest_and_lowest_bids_when_auction_has_three_bids(self):
        jeff = User('Jefferson')
        jorgita = User('Jorgita')
        bid_jeff = Bid(jeff, 150)
        bid_jorgita = Bid(jorgita, 200)
        self.auction.place_bid(self.bid_jorge)
        self.auction.place_bid(bid_jeff)
        self.auction.place_bid(bid_jorgita)

        self.assertEqual(200, self.auction.highest_bid)
        self.assertEqual(100, self.auction.lowest_bid)

    def test_should_place_bid_when_auction_bid_list_is_empty(self):
        self.auction.place_bid(self.bid_jorge)

        self.assertEqual(1, len(self.auction.bids))

    def test_should_place_bid_when_current_and_previous_user_are_different(self):
        jeff = User('Jefferson')
        bid_jeff = Bid(jeff, 150)
        self.auction.place_bid(self.bid_jorge)
        self.auction.place_bid(bid_jeff)

        self.assertEqual(2, len(self.auction.bids))

    def test_should_not_place_bid_when_current_and_previous_user_are_equal(self):
        with self.assertRaises(ValueError):
            self.auction.place_bid(self.bid_jorge)
            self.auction.place_bid(self.bid_jorge)

    def test_should_place_bids_when_added_in_ascending_order(self):
        jeff = User('Jefferson')
        bid_jeff = Bid(jeff, 150)
        self.auction.place_bid(self.bid_jorge)
        self.auction.place_bid(bid_jeff)

        self.assertEqual(2, len(self.auction.bids))

    def test_should_not_place_bids_when_added_in_descending_order(self):
        with self.assertRaises(ValueError):
            jeff = User('Jefferson')
            bid_jeff = Bid(jeff, 150)
            self.auction.place_bid(bid_jeff)
            self.auction.place_bid(self.bid_jorge)
