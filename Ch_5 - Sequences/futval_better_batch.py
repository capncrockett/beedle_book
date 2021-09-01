# future_value_batch.py
#     A program to compute the value of an investment: I/O in batch.

from tkinter.filedialog import askopenfilename, asksaveasfilename


def main():
    print("This program populates a file of client investments from a "
          "file of sorted data.")
    print()

    # get the file names
    infile_name = input("What file are the names in? ")
    # infile_name = askopenfilename()
    outfile_name = input("What file should the usernames go in? ")
    # outfile_name = asksaveasfilename()

    # open the files
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")

    # process each line of the input file
    for line in infile:
        # get the principal, apr, and years from line
        string = line.split(", ")
        principal = int(string[0])
        apr = float(string[1])
        years = int(string[2])

        # create results table
        print("Year    Value", file=outfile)
        print("-" * 15, file=outfile)
        print(f"{0:>2}     ${principal:^8.2f}", file=outfile)

        for i in range(years):
            principal = principal * (1 + apr)
            print(f"{i + 1:>2}     ${principal:^8.2f}", file=outfile)

    # close both files
    infile.close()
    outfile.close()


main()
