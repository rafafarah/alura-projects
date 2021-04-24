from user import User
from bid import Bid
from auction import Auction
from inspector import Inspector

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
    print(f'Higher bid: {inspector.higher_bid}, Lower bid: {inspector.lower_bid}')


if __name__ == "__main__":
    test_inspector()