# goldbach_conjecture.py
import math


def prime_check(n):
    if n < 2:
        return False
    else:
        return all(n % i != 0 for i in range(2, math.isqrt(n) + 1))


def prime_builder(user_int):
    prime_list = []
    for i in range(3, user_int + 1):
        if prime_check(i):
            prime_list.append(i)
        else:
            continue
    return prime_list


def main():
    print("This program checks to see if your number is composed of \n"
          "two primes.")
    # x = int(input("Enter an even number >> "))
    x = 24

    if x % 2 != 0:
        print(f"{x} is not an even number.")
    else:
        print(prime_builder(x))

        for primes_1 in prime_builder(x):
            for primes_2 in prime_builder(x):
                if primes_1 + primes_2 == x:
                    print(primes_1, primes_2)
                else:
                    break


if __name__ == '__main__':
    main()

