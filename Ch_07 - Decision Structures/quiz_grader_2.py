# quiz_grader_2.py
# A better way to program a quiz grader.

def main():
    score = int(input("Enter quiz score (0-5): "))
    grades = "FFDCBA"

    if score == 5:
        print(f"Grade is {grades[5]}")
    elif score == 4:
        print(f"Grade is {grades[4]}")
    elif score == 3:
        print(f"Grade is {grades[3]}")
    elif score == 2:
        print(f"Grade is {grades[2]}")
    else:
        print(f"Grade is F")


main()
