# triangle_area.py
#   Calculates the area of a triangle.

import math


def main():
    print("This program calculates the area of a triangle.")
    print()
    a = float(input("Please enter the length of side a: "))
    b = float(input("Please enter the length of side b: "))
    c = float(input("Please enter the length of side c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of your triangle is ", area)


main()
