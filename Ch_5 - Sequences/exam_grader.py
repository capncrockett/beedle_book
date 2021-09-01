#  exam_grader.py
#   For finding the grade on a 100 point exam.

def main():
    print("Exam Grader")
    score = int(input("Enter the exam score (out of 100): "))
    grades = 60 * "F" + 10 * "D" + 10 * "C" + 10 * "B" + 11 * "A"
    print(f"A score of {score} is a letter grade {grades[score]}.")
    print(grades)


for i in range(10):
    main()
