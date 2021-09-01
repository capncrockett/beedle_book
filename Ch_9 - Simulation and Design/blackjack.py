# blackjack.py
from random import *

# Things to learn from this: I took too many turns trying to make functions.
# This was very unnecessary. The solution code seemed to write from a top
# down kind of approach. As factors presented themselves they were dealt with.
# Mine rambled and tried to incorporate too many elements. I also tried to make
# a deck to deal from. This was not needed. I just wasn't sure how to deal with
# the face cards or the ace itself. This was a learning XP!


def draw_card():
    """Draws one card from the possible options. Assume endless shoe
    for house. Ace will be dealt with in a different function."""
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    draw = randint(0, 12)
    return cards[draw]


def sim_one_game():
    # dealer draws 2 cards
    hand = [draw_card(), draw_card()]
    hand.sort()
    total = sum(hand)

    print(f"Dealer draws {hand[0]} + {hand[1]} = {total}")

    # If dealer has ace
    while has_ace(hand) and (total + 10) < 17 or 17 <= (total + 10) <= 21:
        if has_ace(hand) and 17 <= (total + 10) <= 21:
            total = total + 10
            print(total)
            return False                # If not a bust returns False

        elif (total + 10) < 17:
            hand.append(draw_card())
            total = sum(total)
            if bust(total):             # check for bust
                return True
            else:
                continue

    # If dealer has no ace
    while not bust(total) and must_hit(total):
        hand.append(draw_card())
        print(hand, total)
        if bust(total):
            return True
        else:
            continue

    # while not a bust and < 17 hit
    # return bool bust


def bust(t):
    return t > 21   # t = total


def must_hit(t):
    return t < 17   # t = total


def has_ace(hand):
    """Checks for ace"""
    if 1 in hand:
        return True
    else:
        return False


def main():
    print(sim_one_game())  # Returns True is dealer bust. False otherwise.


main()
