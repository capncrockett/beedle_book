# dateconvert2.py
#     Converts day month and year numbers into two date formats

def main():
    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    # date1 = str(month) + "/" + str(day) + "/" + str(year)
    # date1 = "{0}/{1}/{2}".format(month, day, year)
    date1 = f"{month}/{day}/{year}"
    
    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    month_str = months[month - 1]
    # date2 = month_str + " " + str(day) + ", " + str(year)
    date2 = "{0} {1}, {2}".format(month_str, day, year)

    print("The date is {0} or {1}.".format(date1, date2))


main()
