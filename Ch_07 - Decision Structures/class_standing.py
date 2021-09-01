# class_standing.py
#   A program to calculate a students class standing from number of
#   earned credits.

def main():
    credits = eval(input("Please enter the students total credit: "))

    if credits < 7:
        print("The student is a Freshman")
    elif 7 <= credits <= 15:
        print("The student is a Sophomore")
    elif 16 <= credits <= 25:
        print("The student is a Junior")
    else:
        print("The student is a Senior")


main()
