# maxn.py
#   Finds the maximum of a series of numbers

def main():
    n = int(input("How many numbers are there? "))

    # set nax to be the first value
    maxval = float(input("Enter a number >> "))

    # now compare the n-1 successive values
    for x in range(n - 1):
        x = float(input("Enter a number >> "))
        if x > maxval:
            maxval = x

    print(f"The largest value is {maxval}")


main()

# def main():
#     x1, x2, x3 = eval(input("Please enter three values: "))
#     print(f"The largest value is {max(x1, x2, x3)}")
#
#
# main()
