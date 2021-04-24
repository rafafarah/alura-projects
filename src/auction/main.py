from src.auction.user import User
from src.auction.bid import Bid
from src.auction.auction import Auction
from src.auction.inspector import Inspector

def test_auction():
    jorge = User('Jorge')
    jeff = User('Jefferson')

    bid_jorge = Bid(jorge, 100)
    bid_jeff = Bid(jeff, 150)

    auction = Auction('Cellphone')
    auction.bids.append(bid_jorge)
    auction.bids.append(bid_jeff)

    for bid in auction.bids:
        print(f'User {bid.user.name} has a bid of {bid.value}')

def test_inspector():
    jorge = User('Jorge')
    jeff = User('Jefferson')

    bid_jorge = Bid(jorge, 100)
    bid_jeff = Bid(jeff, 150)

    auction = Auction('Cellphone')
    auction.bids.append(bid_jorge)
    auction.bids.append(bid_jeff)

    inspector = Inspector()
    inspector.inspect(auction)
    print(f'Highest bid: {inspector.highest_bid}, Lowest bid: {inspector.lowest_bid}')


if __name__ == "__main__":
    test_inspector()