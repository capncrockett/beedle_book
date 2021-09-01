# sum_cubes.py
#   A program to sum up the cubes of the natural numbers leading up to,
#   and including, n.

def main():
    print("This program finds the sum of the cubes of the first "
          "natural numbers leading up to, and including, a number.")
    n = int(input("Please enter a whole number: "))
    summed = 0
    for s in range(1, n + 1):
        summed += s ** 3
    print("The sum of the cubes is ", summed)


main()
