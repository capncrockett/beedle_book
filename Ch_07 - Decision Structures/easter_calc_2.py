# easter_calc_2.py
#   A program to calculate the date easter falls on in years 1900-2099.

def main():
    print("Western Easter Calculator (years ???????)")
    year = int(input("Please enter year: "))

    # check if in proper range.
    if 1900 <= year <= 2099:

        # crazy equation to see if easter works.
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        easter = 22 + d + e
        print(a, b, c, d, e)    # FOR TESTING
        print(easter)           # FOR TESTING

        # Special case years that equate to a week too late
        special_cases = [1954, 1981, 2049, 2076]
        if year in special_cases:
            easter = easter - 7

        # if date is greater than 31 print April instead of March.
        if easter > 31:
            print(f"For the year {year} Easter would be on "
                  f"April {easter - 31}")
        else:
            print(f"For the year {year} Easter would be on "
                  f"March {22 + d + e}")

    else:
        print("Please enter a year within 1982-2048")


if __name__ == '__main__':
    main()
