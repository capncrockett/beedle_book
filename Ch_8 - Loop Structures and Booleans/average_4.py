# average_4.py

def main():
    # initialize total to 0.0 and count to 0
    total = 0.0
    count = 0
    # input data item as a string, x_str
    x_str = input("Enter a number (<Enter> to quit) >> ")
    # while x_str is not empty
    while x_str != "":
        # convert x_str to a number, x
        x = float(x_str)
        # add x to total
        total = total + x
        # add 1 to count
        count = count + 1
        # input next data item as a string, x_str
        x_str = input("Enter a number (<Enter> to quit) >> ")
    # output total/ count
    print(f"The average number is {total / count}")


main()
