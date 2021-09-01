# average_5.py

def main():
    file_name = input("What file are the numbers in? ")
    infile = open(file_name, 'r')
    total = 0.0
    count = 0
    for line in infile:
        total = total + float(line)
        count = count + 1
    print(f"The average number is {total / count}")


main()
