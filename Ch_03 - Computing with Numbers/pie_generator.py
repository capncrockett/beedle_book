# pie_generator.py
#   A program to decide what kind of pie you should eat.

import random


def main():
    print()
    print("This program helps you decide which kind of pie you should\n"
          "definitely, surely, without a doubt, eat. It will never be\n"
          "wrong and you will always be happy.... because you will be\n"
          "eating pie!")
    print()
    print("But first you have to answer these three questions.")
    print()
    str(input("1. What is your name? "))
    str(input("2. What is your quest? "))
    str(input("3. What is your favorite color? "))
    print()
    pie = ["Pumpkin", "Pecan", "Pizza Pie", "Apple", "Blueberry",
           "Cherry", "Key Lime"]
    print("You're pie for the day is. . . . {}!"
          .format(random.choice(pie))
          )
    print()
    print("Please enjoy your slice of heaven.")
    print()
    input("Press ENTER to exit...")


main()
