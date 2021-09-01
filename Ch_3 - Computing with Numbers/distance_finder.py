# distance_finder
#   A program to find the distance between two points on a graph.
#

import math


def main():
    print("This program calculates the distance of a graph line.")

    x1, y1 = eval(input("Please enter the 1st set of coordinates "
                        "separated by a comma: "))
    x2, y2 = eval(input("Please enter the 2nd set of coordinates "
                        "separated by a comma: "))
    distance = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    print("The distance of your line is", distance)

    print(type(x1))
    print(type(x2))
    print(type(y1))
    print(type(y2))


main()
