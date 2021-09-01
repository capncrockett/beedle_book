# slope_finder
#   A program to find the slope of two points on a graph.
#
# def main():
#     print("This program calculates the slope of a line.")
#
#     x1, y1 = float(input("Please enter the 1st set of coordinates "
#                         "separated by a comma: "))
#     x2, y2 = float(input("Please enter the 2nd set of coordinates "
#                         "separated by a comma: "))
#     slope = y2 - y1 / x2 - x1
#     print("The slope of your line is", slope)
#
#
# main()
#

def main():
    print("This program calculates the slope of a line.")

    x1, y1 = eval(input("Please enter the 1st set of coordinates "
                        "separated by a comma: "))
    x2, y2 = eval(input("Please enter the 2nd set of coordinates "
                        "separated by a comma: "))
    slope = y2 - y1 / x2 - x1
    print("The slope of your line is", slope)


main()
