# wc.py
#   A Linux like program that runs a line/words/character
#   count on a file.

from tkinter.filedialog import askopenfilename


def main():
    print("This program runs a line/word/character count on a file.")
    print()

    # get file name and open
    f_name = askopenfilename()
    infile = open(f_name, "r")
    # close  file
    infile.close()

    # process each line of the input file
    chars = infile.read()
    words = chars.split()
    lines = chars.split("\n")

    # print it
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {len(chars)}")


main()
