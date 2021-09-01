# sqrt_guesser_func.py
#   Square root using Newton's method.
import math


def sqrt_guesser(x, n):
    guess = x / 2
    for i in range(n):
        guess = (guess + x / guess) / 2
    return guess


def main():
    print("This program calculates square root using Newton's method.")
    print()

    x = float(input("Enter number to find the root of: "))
    n = int(input("How many times should I guess? "))
    print()

    print("Approximate square root:", sqrt_guesser(x, n))
    print("The actual root is:", math.sqrt(x))
    print("Difference from math.sqrt:", math.sqrt(x) - sqrt_guesser(x, n))


main()
