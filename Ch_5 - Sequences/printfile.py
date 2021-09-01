# printfile.py
#   Prints a file to the screen

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)


main()

#
# def main():
#     fname = input("Enter filename: ")
#     infile = open(fname, "r")
#     for i in range(5):
#         line = infile.read()
#         print(line, end="")
#
#
# main()
#
# def main():
#     fname = input("Enter filename: ")
#     infile = open(fname, "r")
#     for line in infile:
#         line = infile.read()
#         print(line)
#
#
# main()
