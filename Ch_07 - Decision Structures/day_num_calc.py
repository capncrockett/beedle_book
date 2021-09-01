# day_num_calc.py
#   This program calculates the day number in a given year.
from valid_date_func import valid_date
from leap_year_func import leap_year


def day_of_the_year(month: int, day: int, year: int) -> int:
    # three steps to equate:
    day_num = 31 * (month - 1) + day

    if month > 2:
        day_num = day_num - (4 * month + 23) // 10

    if leap_year(year):
        if month > 2:
            day_num = day_num + 1

    return day_num


def main():
    print("Day of the year calculator.\n")
    # accept input from user. A date in the form of MM/DD/YYYY:
    # make sure date is valid with our fancy function.
    month, day, year = input("Enter a date in format MM/DD/YYYY: ").split("/")

    if valid_date(int(month), int(day), int(year)):
        print(f"Day number {day_of_the_year(int(month), int(day), int(year))} "
              f"of the year.\n")
    else:
        print("Date is Invalid\n")


for i in range(10):
    main()
