# c09ex08.py
#    Simulation to Blackjack dealer to estimate bust probability.
from random import randrange


def main():
    print("Simulation of a Blackjack dealer.\n")
    n = int(input("How many trials? "))
    busts = 0
    for i in range(n):
        points = deal_hand()
        if points > 21:
            busts = busts + 1
    print("In %d hands dealer busted %d times." % (n, busts))
    print("Estimated prob =", float(busts)/n)


def deal_hand():
    total = 0
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
