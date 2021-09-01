# pizza_slice_cost.py
#   Calculates the price for a slice.

import math


def cost_per_sq_in(d: float, p: float) -> float:
    radius = d / 2
    area = math.pi * radius ** 2
    result = p / area
    return round(result, 2)


print("This program finds the cost per square inch of a slice of "
      "pizza given its price and diameter.")
print()
price = float(input("Enter the price: "))
size = float(input("Enter the size: "))
print()
print("The cost per square inch is ", cost_per_sq_in(price, size))
