# leap_year_func.py
#   Leap Year calculator.

def leap_year(year: int) -> bool:
    if year % 4 != 0:        # Regular check for leap year.
        return False
    elif year % 100 == 0:    # Check for century year.
        if year % 400 == 0:  # Check for century divisibility by 400.
            return True
        else:
            return False
    else:
        return True


# def main():
#     print("Leap Year Calculator\n")
#     year = int(input("Enter a year: "))
#
#     leap_year(year)
#     if leap_year(year) is True:
#         print(f"{year} is a leap year :)")
#     else:
#         print(f"{year} is not a leap year :(")
#
#
# for i in range(10):
#     main()
