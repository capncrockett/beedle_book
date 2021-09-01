# easter_calc_1.py
#   A program to calculate the date easter falls on in years 1982-2048.

print("Western Easter Calculator (years 1982-2048)")
# input: year
year = int(input("Please enter year: "))

# check if in proper range.
if 1982 <= year <= 2048:

    # crazy equation to see if easter works.
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    easter = 22 + d + e
    print(a, b, c, d, e)    # FOR TESTING
    print(easter)           # FOR TESTING

    # if date is greater than 31 print April instead of March.
    if easter > 31:
        print(f"For the year {year} Easter would be on "
              f"April {easter - 31}")
    else:
        print(f"For the year {year} Easter would be on "
              f"March {22 + d + e}")

else:
    print("Please enter a year within 1982-2048")
