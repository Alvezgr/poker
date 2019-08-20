"""poker hands module"""


def poker(hands):
    """return the best hand: poker([hand, ...]) => hand"""
    return max(hands, key=hand_rank)


def hand_rank(hand):
    "define the rank of a hand"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))


def test():
    "Test cases for functions in poker program"
    sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf

    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh

    assert poker([sf]) == sf
    assert poker([sf + 99*[fh]]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "tests pass"

if __name__ == '__main__':
    print(test())
