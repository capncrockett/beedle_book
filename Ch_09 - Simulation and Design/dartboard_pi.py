# dartboard_pi.py
#   A program that estimates Pi by throwing darts at a dart board.
from random import random


def throw_darts(d):
    hits = outside = 0
    for i in range(d):
        x = 2 * random() - 1
        y = 2 * random() - 1
        if (x ** 2) + (y ** 2) <= 1:
            hits = hits + 1
        else:
            outside = outside + 1

    return hits, outside


def main():
    print("This program uses Monte Carlo to estimate Pi by throwing \n"
          "darts randomly.")
    darts = int(input("How many darts would you like to throw? "))

    hits, outside = throw_darts(darts)

    print(f"\nTotal Darts = {darts}")
    print(f"Inside = {hits}")
    print(f"Outside = {outside}")

    pi = 4 * (hits / darts)

    print(f"Pi is ~ {pi}")


if __name__ == '__main__':
    main()
