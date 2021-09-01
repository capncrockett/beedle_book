# blackjack_2.py
#    Simulation of Blackjack dealer to estimate bust probability given
#    first showing card.
from random import randrange
import operator


def main():
    print("Simulation of a Blackjack dealer.")
    print("Bust probabilities given card showing.\n")
    n = int(input("How many trials? "))
    bj_probs = {}

    for showing in range(1, 11):
        busts = 0
        for i in range(n):
            points = deal_hand(showing)
            if points > 21:
                busts = busts + 1
        bust_prob = float(busts) / n
        print(f"In {n} hands dealer busted {busts} times showing {showing}.")
        print(f"Estimated prob = {bust_prob:0.1%}")

        bj_probs[showing] = bust_prob

    print(bj_probs)
    print(f"Best Odds with {max(bj_probs, key=bj_probs.get)} showing.")


def deal_hand(showing):
    total = 0 + showing
    have_ace = False
    while total < 17:
        card = randrange(1, 14)
        if card == 1:
            have_ace = True
        total = total + bj_value(card)
        if have_ace:
            total = adjust_for_ace(total)
    return total


def bj_value(card):
    if card > 10:
        return 10
    else:
        return card


def adjust_for_ace(total):
    if 16 < total + 10 < 22:
        return total + 10
    else:
        return total


if __name__ == '__main__':
    main()
