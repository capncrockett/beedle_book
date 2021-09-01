# ladder_height.py
#   Program calculates the needed ladder height to reach the top of a
#   roof given the roof height and angle in radians.

import math


def main():
    print("This program helps you figure out what length ladder you're "
          "gonna need.")
    print()
    height = eval(input("Enter the height of the roof in feet: "))
    degrees = eval(input("Enter the angle, in degrees, of the lean: "))
    radians = (math.pi / 180) * degrees
    length = round(height / math.sin(radians), 1)
    print("You will need a {} foot ladder.".format(length))


main()
