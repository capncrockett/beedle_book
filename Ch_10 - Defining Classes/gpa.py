# gpa.py
#   Program to find student with the highest GPA

class Student:
    def __init__(self, name, hours, q_points):
        self.name = name
        self.hours = float(hours)
        self.q_points = float(q_points)

    def get_name(self):
        return self.name

    def get_hours(self):
        return self.hours

    def get_q_points(self):
        return self.q_points

    def gpa(self):
        return self.q_points / self.hours


def make_student(info_str):
    """"
    info_str is a tab-separated line: name hours q_points
    returns a corresponding Student object
    """
    name, hours, q_points = info_str.split("\t")
    return Student(name, hours, q_points)


def main():
    # open the input file for reading
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')

    # set best to the record for the first student in the file
    best_list = []
    best = make_student(infile.readline())
    best_list.append(best)

    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = make_student(line)
        # if this student is best so far, remember it.
        if s.gpa() == best.gpa():
            best_list.append(s)
            best = s
        elif s.gpa() > best.gpa():
            best_list.clear()
            best_list.append(s)
            best = s

    infile.close()

    # print information about the best student
    if len(best_list) == 1:
        print(f"The best student is: {best.get_name()}")
        print(f"hours: {best.get_hours()}")
        print(f"GPA: {best.gpa()}")
    else:
        print(f"The best students are:")
        for student in best_list:
            print(f"{student.get_name()}")
            print(f"hours: {student.get_hours()}")
            print(f"GPA: {student.gpa()}")


if __name__ == '__main__':
    main()
