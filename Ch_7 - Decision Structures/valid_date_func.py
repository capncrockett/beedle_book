# valid_date_func.py
#   A program to check if user input is a valid date. It doesn't take
#   into account negative numbers for years.
from leap_year_func import leap_year


def valid_date(month: int, day: int, year: int) -> bool:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12:
        # Month is OK. Move on.

        # Determine last day in month.
        if month == 2:
            if leap_year(year):
                last_day = 29
            else:
                last_day = 28
        else:
            last_day = days_in_month[month - 1]

        # if day is also good, return True
        if 1 <= day <= last_day:
            return True
    else:
        return False


# def main():
#     print("This program determines if a date input is valid.")
#     month, day, year = input("Enter a date in format MM/DD/YYYY: ").split("/")
#
#     if valid_date(int(month), int(day), int(year)):
#         print("Date Valid.")
#     else:
#         print("Date is Invalid")
#
#
# for i in range(10):
#     main()
