from src.auction.user import User
from src.auction.auction import Auction

def test_should_subtract_from_user_wallet_when_bid_is_placed():
    jorge = User("Jorge", 100)
    auction = Auction("Cellphone")

    jorge.place_bid(auction, 50)

    assert 50 == jorge.wallet