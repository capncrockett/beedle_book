# quadratic_4.py
#   A program that computes the real roots of a quadratic equation.

import math  # Makes the math library available.


def main():
    print("This program finds the real solutions to a quadratic\n")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots!")
    elif discrim == 0:
        root = -b / (2 * a)
        print(f"\nThere is a double root at {root}")
    else:
        disc_root = math.sqrt(discrim)
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print(f"The solutions are: {root1} and {root2}")


main()
