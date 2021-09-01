# sum_up_to.py
#   Program to sum up all whole numbers up to n inclusive.

def main():
    print("This program finds the sum of all natural numbers "
          "preceding, and including, a number.")
    n = int(input("Enter a whole number to sum with all preceding "
                  "whole numbers: "))
    summed = 0
    for i in range(1, n + 1):
        summed += i
    print("The sum is ", summed)


main()
