# prime_checker.py
#   A positive number n > 2 is prime if no num between 2 and
#   the sqrt of n (inclusive) evenly divides n.
import math


def prime_check(n):
    sqrt_n = int(math.sqrt(n))

    if n > 2:
        if n == 3:
            print("3 is prime")
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                print(f"{n} can be divided by {i}")
                break
            elif n % i != 0 and i == sqrt_n:
                print(f"{n} is prime")


def main():
    print("This program checks to see if a number is prime.\n")
    x = int(input("Enter a positive, whole number greater than 2 >> "))
    prime_check(x)


if __name__ == '__main__':
    main()
