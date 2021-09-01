# quadratic_5.py
#   A program that computes the real roots of a quadratic equation.
import math


def main():
    print("This program finds the real solutions to a quadratic\n")
    # try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    disc_root = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + disc_root) / (2 * a)
    root2 = (-b - disc_root) / (2 * a)
    print(f"The solutions are: {root1} and {root2}")
    # except ValueError as excObj:
    #     if str(excObj) == "math domain error":
    #         print("No real roots")
    #     else:
    #         print("Invalid coefficient given")
    # except:
    #     print("\nSomething went wrong, sorry!")


main()
