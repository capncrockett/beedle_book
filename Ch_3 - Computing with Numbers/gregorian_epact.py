# gregorian_epact.py
#   Program calculates the days between January 1st and the previous
#   new moon. This value is used to figure out the date of Easter.

def main():
    print("How do we calculate the date of Easter? Well, Christians \n"
          "are kinda weird, but this program will help us figure it \n"
          "out anyways.")
    print()
    year = int(input("Enter a 4 digit year to find out the date: "))
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25)
             + 11 * (year % 19)) % 30

    print("The epact value is {} days.".format(epact))


def main2():
    print("This program calculates the Gregorian epact value of year.")
    print()

    year = int(input("Enter the year (e.g. 2020): "))
    c = year // 100
    epact = (8+(c//4) - c + ((8*c + 13)//25) + 11 * (year % 19)) % 30

    print()
    print("The epact value is", epact, "days.")


main()
main2()
