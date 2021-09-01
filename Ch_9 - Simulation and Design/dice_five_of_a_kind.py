# dice_five_of_a_kind.py
#   Estimates the odds of rolling five of a kind in a single roll of
#   five six-sided dice.
from random import randrange

# TODO Rewrite roll_em as for loop based on solution. Append list to dict outside of function.


def d6():
    """Returns the roll of a 6-sided die."""
    return randrange(1, 7)


def roll_em(n):
    foak = 0

    rolls = {}

    for i in range(n):
        d_1 = d6()                          # roll first dice
        d_2 = d6()                          # roll second dice
        rolls[i] = [d_1, d_2]

        if d_1 == d_2:                      # if 1 and 2 match
            d_3 = d6()                      # roll third dice
            rolls[i].append(d_3)

            if d_3 == d_2:                  # if 2 and 3 match
                d_4 = d6()                  # roll fourth dice
                rolls[i].append(d_4)

                if d_4 == d_3:              # if 3 and 4 match
                    d_5 = d6()              # roll fifth dice
                    rolls[i].append(d_5)

                    if d_5 == d_4:          # if 5th matches it's a FOAK!
                            foak = foak + 1
        else:
            continue

    return foak, rolls


def main():
    print("\nThis program simulates your odds of rolling a five of a "
          "kind in one roll using only six-sided dice.")
    rolls = int(input("How many rolls would you like to try? "))
    foak, rolls_dict = roll_em(rolls)

    two_oak = three_oak = four_oak = 0
    for k, v in rolls_dict.items():
        print(f"Roll {k + 1}: {v}")
        if len(v) == 2:
            two_oak = two_oak + 1
        elif len(v) == 3:
            three_oak = three_oak + 1
        elif len(v) == 4:
            four_oak = four_oak + 1
    print(25 * "*")

    print(f"\nTwo OAKs = {two_oak}")
    print(f"Three OAKs = {three_oak}")
    print(f"Four Oaks = {four_oak}")
    print(f"\nFOAKs in one roll = {foak}")
    print(f"Your odds are {foak / rolls:0.2%}")


if __name__ == '__main__':
    main()


# # c09ex11.py
# #     Probability of rolling 5 of a kind
#
# from random import randrange
#
# def main():
#     print("This program estimates the probability of rolling")
#     print("five of a kind on a single roll of 5 dice.\n")
#
#     n = int(input("How many rolls should I simulate? "))
#     hits = 0
#     for i in range(n):
#         if equalRolls(5):
#             hits = hits + 1
#     print("Estimated prob =", float(hits)/n)
#
#
# def equalRolls(count):
#     # count is number of dice to be rolled (must be >1)
#     # returns True if all values turn out the same, False o/w
#     first = randrange(1,7)
#     for i in range(count-1):
#         roll = randrange(1,7)
#         if roll != first:
#             return False
#     # All rolls were equal to the first
#     return True
#
# if __name__ == '__main__':
#     main()
#
