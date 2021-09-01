# numerology_102
#   A program to determine your numerological worthiness to exist.

def main():
    print("Welcome to your numerological valuator.")
    name = input("Please enter a full name: ")
    total = 0
    for char in name:
        letters = " abcdefghijklmnopqrstuvwxyz".split(char.lower())
        value = len(letters[0])
        total = total + value
    print(f"Your numerological value is {total}.")


main()

# c05ex06.py
#     Numerology of a full name
#
#
# def main():
#     print("This program computes the 'number value' of a name")
#     print()
#
#     names = input("Enter a name: ")
#
#     # Create a string of all the letters -- avoids nested loop
#     letters = "".join(names.split())
#     total = 0
#     for letter in letters:
#         total = total + ord(letter.lower()) - ord('a') + 1
#
#     print("The value is:", total)
#
#
# main()

# # numerology_101
# #   A program to determine your numerological worthiness to exist.
#
# def main():
#     print("Welcome to your numerological valuator.")
#     name = input("Please enter a name: ")
#     total = 0
#     for char in name:
#         letters = "abcdefghijklmnopqrstuvwxyz".split(char)
#         value = len(letters[0]) + 1
#         total = total + value
#     print(f"Your numerological value is {total}.")
#
#
# main()

# # c05ex05.py
# #     Numerology of a single name
#
#
# def main():
#     print("This program computes the 'number value' of a name")
#     print()
#
#     name = input("Enter a single name: ")
#     total = 0
#     for letter in name:
#         total = total + ord(letter.lower()) - ord('a') + 1
#
#     print("The value is:", total)
#
#
# main()
