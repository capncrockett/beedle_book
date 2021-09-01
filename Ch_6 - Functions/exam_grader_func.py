#  exam_grader_func.py
#   For finding the grade on a 100 point exam.

def letter_grade(score: int) -> str:
    grades = 60 * "F" + 10 * "D" + 10 * "C" + 10 * "B" + 11 * "A"
    return grades[score]


def main():
    print("Exam Grader")
    score = int(input("Enter the exam score (out of 100): "))
    print(f"A score of {score} is a letter grade {letter_grade(score)}.")
    print()


for i in range(10):
    main()
