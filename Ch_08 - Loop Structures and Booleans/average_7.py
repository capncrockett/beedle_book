# average_7.py

def main():
    file_name = input("What file are the numbers in? ")
    infile = open(file_name, 'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        # update total and count for values in line
        for x_str in line.split(","):
            total = total + float(x_str)
            count = count + 1
        line = infile.readline()
    print(f"The average number is {total / count}")


main()
