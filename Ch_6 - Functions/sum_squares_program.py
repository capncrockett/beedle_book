# sum_squares_program.py
#   This program sums the squares of a list_of_numbers from a given
#   text file.

def mod_to_num(str_list):
    """Returns string numbers to float. Modified list."""
    for i in range(len(str_list)):
        str_list[i] = float(str_list[i])


def square_each(nums):
    """Squares numbers from a list in place. Returns modified list."""
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    total = 0
    for i in nums:
        total = total + i
    return total


def main():
    print("Program to find sum of squares from numbers in a file.")
    fname = input("Enter filename: ")

    # infile = open(fname, "r")
    # data = infile.readlines()

    data = open(fname, 'r').readlines()

    mod_to_num(data)
    print(data)

    square_each(data)
    print(data)

    print(sum_list(data))


main()
