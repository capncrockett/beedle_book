# exam_grader_2.py
#   A different exam grader using if-elif-else.

def main():
    score = int(input("Enter student exam score: "))

    if 100 >= score >= 90:
        print("Grade is A")
    elif 89 >= score >= 80:
        print("Grade is B")
    elif 79 >= score >= 70:
        print("Grade is C")
    elif 69 >= score >= 60:
        print("Grade is D")
    elif 59 >= score >= 0:
        print("Grade is F")
    else:
        print("Score is not valid. Please check again.")


main()
