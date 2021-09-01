# maxval.py
#   A program to determine the highest of three numbers

def main():
    print("Enter three numbers...")
    x1 = eval(input("Enter a number: "))
    x2 = eval(input("Enter a number: "))
    x3 = eval(input("Enter a number: "))

    maxval = 0
    if x1 >= x2 and x1 >= x3:
        maxval = x1
    elif x2 >= x1 and x2 >= x3:
        maxval = x2
    elif x3 >= x1 and x3 >= x2:
        maxval = x3

    print(maxval)


main()
