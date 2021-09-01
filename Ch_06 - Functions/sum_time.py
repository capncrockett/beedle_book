# sum_time.py

def sum_up_to(n):
    summed = 0
    for i in range(1, n + 1):
        summed += i
    print(f"The sum is {summed}.")


def sum_up_cubes(n):
    summed = 0
    for s in range(1, n + 1):
        summed += s ** 3
    print(f"The sum of the cubes is {summed}")


def main():
    print("This program sums up the first n natural numbers and the \n"
          "sum of the cubes of the first n natural numbers.\n")
    n = int(input("Please enter a value for n: "))
    sum_up_to(n)
    sum_up_cubes(n)


main()
