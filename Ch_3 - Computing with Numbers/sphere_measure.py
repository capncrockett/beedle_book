# sphere_measure.py
#   A program for finding the volume and surface area of a sphere.

import math  # Makes the math library available.


def volume(r: float) -> float:
    """Get volume of a sphere given `r`. Rounds to nearest 100th."""
    result = round(4 / 3 * math.pi * r ** 3, 2)
    return result


def surface_area(r: float) -> float:
    """Get surface area of a sphere given `r`. Rounds to nearest
    100th"""
    result = round(4 * math.pi * r ** 2, 2)
    return result


print("This program finds the volume and surface area of a sphere.")
print()
radius = float(input("Enter radius: "))
print("The volume is {}".format(volume(radius)))
print("The area is {}".format(surface_area(radius)))
