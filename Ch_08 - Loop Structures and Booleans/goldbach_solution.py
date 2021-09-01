# c08ex07.py
#    Goldbach tester
from prime_check_accumulator import prime_check


def goldbach(x):
    cand = 3
    while cand < x/2:
        other = x - cand
        if prime_check(cand) and prime_check(other):
            return cand
        cand = cand + 2


def main():
    print("Goldbach checker\n")

    n = int(input("Enter an even natural number: "))
    if n % 2 != 0:
        print(f"{n} is not even!")
    else:
        prime_1 = goldbach(n)
        prime_2 = n - prime_1
        print(f"{prime_1} + {prime_2} = {n}")


if __name__ == '__main__':
    main()
