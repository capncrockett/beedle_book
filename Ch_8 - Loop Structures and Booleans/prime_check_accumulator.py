# prime_check_accumulator.py
#   A positive number n > 2 is prime if no num between 2 and
#   the sqrt of n (inclusive) evenly divides n.
import math


def prime_check(n):
    if n < 2:
        return False
    else:
        return all(n % i != 0 for i in range(2, math.isqrt(n) + 1))


def main():
    print("This program returns all prime numbers less than or equal \n"
          "to your magical number!!!.\n")
    x = int(input("Enter a positive, whole number greater than 2 >> "))

    if prime_check(x):
        print(f"{x} is prime")
    else:
        print(f"{x} is not prime\n")

    prime_list = []
    for i in range(3, x + 1):
        if prime_check(i):          # If number is prime append to list.
            prime_list.append(i)
        else:                       # If not prime continue.
            continue

    # Print out all the primes fancy like.
    print("The following are all prime numbers <= your number...")
    print(*prime_list, sep=", ")
    print("Have a nice day")


if __name__ == '__main__':
    main()
