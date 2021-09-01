# # pizza_functions.py
# #   Calculates area and cost per square inch.
import math


def find_area(diameter: float) -> float:
    return math.pi * (diameter * 0.5) ** 2


def cost_per_sq_in(price: float, diameter: float) -> float:
    return price / find_area(diameter)


def main():
    print("This program finds the area and cost per square inch of a \n"
          "slice of pizza given its price and diameter.\n")

    price = float(input("Enter the price: "))
    diameter = float(input("Enter the size (diameter): "))
    print()
    print(f"Pizza area: "
          f"{round(find_area(diameter))} square inches.\n"
          f"Cost per square inch: "
          f"{round(cost_per_sq_in(price, diameter), 2)}.")


main()


# # c06ex05.py
# #    Pizza value with functions
#
#
# import math
#
#
# def costPer(d, price):
#     return float(price) / area(d)
#
# def area(d):
#     return math.pi * (0.5*d)**2
#
# def main():
#     print("Program to calculate the value of a pizza\n")
#
#     diam = float(input("Enter the diameter of the pizza: "))
#     cost = float(input("Enter the price of the pizza: "))
#
#     print("\nThe pizza costs %0.4f per square unit." % (costPer(diam,cost)))
#
# main()
