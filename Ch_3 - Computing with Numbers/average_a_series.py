# average_a_series
#   A program to calculate the average of a series of numbers.

def main():
    print("This program can find the average of your numbers.")
    number_count = int(input("How many numbers will we be working with "
                             "today? "))
    summed = 0
    for i in range(number_count):
        x = float(input("Enter a number: "))
        summed += x
    average = float(summed / number_count)
    print()

    print("The average is ", average)


main()
