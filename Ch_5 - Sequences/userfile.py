# userfile.py
#   Program to create a file of username in batch mode.

from tkinter.filedialog import askopenfilename, asksaveasfilename


def main():
    print("This program creates a file of usernames from a file "
          "of names.")
    print()

    # get the file names
    # infile_name = input("What file are the names in? ")
    infile_name = askopenfilename()
    # outfile_name = input("What file should the usernames go in? ")
    outfile_name = asksaveasfilename()

    # open the files
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the username
        uname = (first[0] + last[:7]).lower()
        # write it to the output file
        print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()


main()
