# sum_a_series
#   A program to sum up a series of numbers provided from a user.

def main():
    print("This program sums up a user submitted series of numbers.")
    number_count = int(input("How many numbers will we be summing"
                             "up today? "))
    summed = 0
    for i in range(number_count):
        x = float(input("Enter a number: "))
        summed += x
    print("The sum of the numbers is ", summed)


main()
