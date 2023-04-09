from src.auction.user import User
from src.auction.auction import Auction
from src.auction.exceptions import InvalidBid
import pytest

@pytest.fixture
def jorge():
    return User("Jorge", 100)

@pytest.fixture
def auction():
    return Auction("Cellphone")

def test_should_subtract_from_user_wallet_when_bid_is_placed(jorge, auction):
    jorge.place_bid(auction, 50)

    assert 50 == jorge.wallet

def test_shoud_place_bid_when_wallet_balance_is_greater_than_bid(jorge, auction):
    jorge.place_bid(auction, 1)

    assert 99 == jorge.wallet

def test_shoud_place_bid_when_wallet_balance_is_equal_to_bid(jorge, auction):
    jorge.place_bid(auction, 100)

    assert 0 == jorge.wallet

def test_shoud_not_place_bid_when_wallet_balance_is_less_than_bid(jorge, auction):
    with pytest.raises(InvalidBid):
        jorge.place_bid(auction, 150)
