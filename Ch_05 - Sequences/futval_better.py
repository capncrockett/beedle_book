# future_value.py
#     A program to compute the value of an investment
#   carried 10 years in to the future.

def main():
    print("This program calculates the future value of an investment.")
    print()

    principal = eval(input("Enter the investment amount: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the investment time in years: "))

    # FOR TESTING
    # principal = 2000
    # apr = 0.1
    # years = 20

    print(f"Year    Value")
    print("-" * 15)
    print(f"{0:>2}     ${principal:^8.2f}")

    for i in range(years):
        principal = principal * (1 + apr)
        print(f"{i + 1:>2}     ${principal:^8.2f}")


main()
