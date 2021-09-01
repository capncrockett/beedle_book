# pi_approx
#   Program approximates the value of pi.
import math


def main():
    print("This program approximates the value of pi by summing a fixed")
    print("number of terms in a series.")
    print()

    n = int(input("How many terms should I use? "))

    total = 0.0
    sgn = 1.0   # used to alternate sign of terms
    for denom in range(1, 2*n, 2):
        total = total + sgn * 4.0/denom
        sgn = -sgn  # flip the sign

    print("Approximation to pi is:", total)
    print("Difference from math.pi:", math.pi - total)

    # print("This program approximates the value of pi to a defined "
    #       "amount of spaces...?")
    # n = int(input("Enter a value for n: "))
    #
    # pi = 0
    # x = 1
    # for i in range(n):
    #     total1 = 4 / x
    #     pi += total1
    #
    #     x = x + 2
    #     total2 = total1 - 4 / x
    #
    #     pi += total2
    #
    # print("The approximate value of pi for {} spaces is {}."
    #       .format(n, pi))


main()
