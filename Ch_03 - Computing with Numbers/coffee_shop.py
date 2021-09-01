# coffee_shop
#   Program to calculate the cost of a shipping order per pound.

def main():
    print("This program calculates the price per pound of coffee if you "
          "wish to make a purchase from the Konditorei coffee company.")
    print()
    desired_pounds = float(input(
        "Please tell us how many pounds you'd like to order: "))
    cost_per_pound = 10.50
    shipping_cost = desired_pounds * 0.86 + 1.5
    total = round(desired_pounds * cost_per_pound + shipping_cost, 2)
    print()
    print("Your total will be ${}".format(total))


main()
