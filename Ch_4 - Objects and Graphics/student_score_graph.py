# student_score_graph.py
#   Program to plot a bar chart of student scores.

from tkinter.filedialog import askopenfilename
from graphics import *


def main():
    print("This program draws a bar graph for your students scores.")
    print()

    # get file name and open
    f_name = 'C:/Users/capnc/OneDrive/Programming/Beedle Book/Chapter 5 - Sequences/student_scores.txt'
    # f_name = askopenfilename()
    # infile = open(f_name, "r", newline='\n')
    infile = open(f_name, "r")

    total_students = 0
    for aline in infile:
        values = aline.split()
        print('Student', values[0], 'has a score of', values[1])
        total_students = total_students + 1

    print(f"There are {total_students} total students.")

    # close  file
    infile.close()


main()
