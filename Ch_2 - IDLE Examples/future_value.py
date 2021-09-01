# future_value.py
#     A program to compute the value of an investment
#   carried 10 years in to the future.
#
# def main():
#     print("This program calculates the future value of an investment.")
#
#     principal = eval(input("Enter the initial principal: "))
#     apr = eval(input("Enter the annual interest rate: "))
#     years = eval(input("Enter the investment time in years: "))
#     principal_init = principal
#     for i in range(years):
#         principal *= (1 + apr)
#
#     print("The total value in {} years is:".format(years), int(principal))
#     print("The value from interest in {} years is:".format(years),
#           int(principal - principal_init))
#
#
# main()
#
# def main():
#     print("This program calculates the future value of an investment.")
#     print()
#
#     payment = eval(input("Enter the yearly investment amount: "))
#     apr = eval(input("Enter the annual interest rate: "))
#     years = eval(input("Enter the investment time in years: "))
#
#     principal = 0.0
#     for i in range(years):
#         principal = (principal + payment) * (1 + apr)
#
#     print("The amount in", years, "years is:", principal)
#     print("The value from interest in {} years is:".format(years),
#           (principal - (payment * years)))
#
#
# main()
def main():
    print("This program calculates the future value of an investment"
          "over a set amount of periods.")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding "
                         "periods each year: "))
    years = eval(input("Enter the number of years: "))

    for i in range(10 * periods):
        principal = principal * (1 + rate / periods)

    print("The amount in {} years is:".format(years), principal)


main()
