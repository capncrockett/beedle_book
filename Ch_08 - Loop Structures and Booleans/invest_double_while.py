# invest_double_while.py
#   A program using a while loop to determine how long it takes for an
#   investment to double at a given interest rate.

# input: annualized interest rate
# output  number of years it takes an investment to double.
# note: the amount of the initial investment does not matter
# (could be $1).

print("This program calculates how long it will take for your \n"
      "investment to double given a certain interest rate. For ease \n"
      "of understanding we have chosen the principal amount of $1.\n")

apr = float(input("What is the interest rate? "))
# apr = 0.06      # FOR TESTING
print()
principal = 1
doubled = principal * 2
years = 0

while principal <= doubled:
    principal = principal + (principal * apr)
    years = years + 1
    print(f"Year {years:2.0f}: Principal = ${principal:2.2f}")

print(f"\nWith an apr of {apr * 100}% it will take {years} years for your "
      f"investment to double.")
