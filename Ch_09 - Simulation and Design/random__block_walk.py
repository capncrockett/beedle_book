# random_walk.py
import random


def four_directions():
    return random.choice(['n', 's', 'e', 'w'])


def walking(n):
    pos_x = pos_y = 0
    position = 0

    for i in range(n):
        choice = four_directions()
        print(choice)

        if choice == 'n':
            pos_y = pos_y + 1
        elif choice == 's':
            pos_y = pos_y - 1
        elif choice == 'e':
            pos_x = pos_x + 1
        else:
            pos_x = pos_x - 1

        position = pos_x, pos_y
        print(position)

    return position


def main():
    print("\nThis program takes a random walk around the block. Roll \n"
          "a four-sided dice to decide your direction (NSEW).")
    steps = int(input("How many times would you like to roll the dice? "))
    # steps = 10

    start = (0, 0)
    end = walking(steps)

    distance = tuple(map(lambda x, y: x - y, start, end))

    print(f"You moved {distance} from the starting position of (0, 0)")


if __name__ == '__main__':
    main()

# # c09ex13.py
# #    Random block walking
#
# from random import randrange
#
# def main():
#     print("Simulation of two dimensional random walk\n")
#
#     walks = int(input("How many walks should I do? "))
#     steps = int(input("How many steps should I take on each? "))
#
#     totalDist = 0
#     for i in range(walks):
#         thisDist = randomWalk2D(steps)
#         totalDist = totalDist + thisDist
#
#     print("Average distance from start", totalDist/walks)
#
#
# def randomWalk2D(n):
#     x, y = 0, 0   # start at the origin
#     for i in range(n):
#         dir = randrange(4)
#         if dir == 0:    # go left
#             x = x - 1
#         elif dir == 1:  # go up
#             y = y + 1
#         elif dir == 2:  # go right
#             x = x + 1
#         else:           # go down
#             y = y - 1
#
#     return (x * x + y * y) ** .5    # distance to origin
#
#
# if __name__ == '__main__':
#     main()
