#  quiz_grader.py
#  This is a program to grade quiz scores.

def main():
    quiz_score = int(input("Enter the quiz score: "))
    grades = ["F", "F", "D", "C", "B", "A"]
    quiz_grade = grades[quiz_score]
    print(f"The letter grade is {quiz_grade}.")


main()

# c05ex02.py
#    Quiz grader


def main():
    print("Five point quiz grader")
    score = int(input("Enter the score: "))
    grade = "FFDCBA"[score]
    print("The grade is", grade)


main()
