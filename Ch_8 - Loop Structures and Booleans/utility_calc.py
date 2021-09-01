# utility_calc.py
#   A program that accepts a sequence of average daily temperatures and
#   computes the running total of cooling and heating degree days.

def main():
    print("Heating and cooling degree days calculator.\n")

    cooling_days = 0
    heating_days = 0
    temp_string = input("Enter daily temps (<ENTER> to finish): ")

    while temp_string != "":
        temp = float(temp_string)
        if temp < 60:
            heating_days = heating_days + (60 - temp)
        if temp > 80:
            cooling_days = cooling_days + (temp - 80)
        temp_string = input("Enter daily temps (<ENTER> to finish): ")

    print(f"Cooling days: {cooling_days}")
    print(f"Heating days: {heating_days}")


if __name__ == '__main__':
    main()

# cooling and heating days running total
# input: daily temps
# process: compute average cooling, heating
# cooling days: for every degree under 60 add to heating day.
# heating days: for every degree over 80 add to cooling day.


# c08ex11.py
#    heating/colling degree-days
#
#
# def main():
#     print("Heating and Cooling degree-day calculation.\n")
#
#     heating = 0.0
#     cooling = 0.0
#     temp_str = input("Enter an average daily temperature: ")
#     while temp_str != "":
#         temp = float(temp_str)
#         heating = heating + max(0, 60 - temp)
#         cooling = cooling + max(0, temp - 80)
#         temp_str = input("Enter an average daily temperature: ")
#
#     print("\nTotal heating degree-days", heating)
#     print("Total cooling degree-days", cooling)
#
#
# if __name__ == '__main__':
#     main()
