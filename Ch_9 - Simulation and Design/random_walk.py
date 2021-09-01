# random_walk.py
import random


def coin_flip():
    # return random.choice([True, False])   # Far more readable
    return bool(random.getrandbits(1))      # Actually faster


def walking(n):
    forward = backward = 0

    for i in range(n):
        if coin_flip():
            forward = forward + 1
        else:
            backward = backward + 1
    return forward, backward


def main():
    print("\nThis program takes a random walk. Flip a coin n times. \n"
          "If heads take a step forward, if tails take a step back.\n")
    steps = int(input("How many times would you like to flip the coin? "))

    forward, backward = walking(steps)
    moved = forward - backward

    if moved < 0:
        x = "backwards"
    elif moved > 0:
        x = "forwards"
    else:
        x = "and stood still..."

    print(f"Forward steps: {forward}")
    print(f"Backward steps: {backward}")
    print(f"You moved a total of {abs(moved)} steps {x}")


if __name__ == '__main__':
    main()

# # c09ex12.py
#
# from random import random
#
# def main():
#     print("Simulation of random walk in one dimension.\n")
#
#     walks = int(input("How many walks should I do? "))
#     steps = int(input("How many steps should I take on each? "))
#
#     totalDist = 0
#     for i in range(walks):
#         thisDist = randomWalk(steps)
#         totalDist = totalDist + thisDist
#
#     print("Average distance from start", totalDist/walks)
#
#
# def randomWalk(n):
#     pos = 0
#     for i in range(n):
#         if random() <.5:
#             pos = pos - 1
#         else:
#             pos = pos + 1
#     return abs(pos)
#
#
# if __name__ == '__main__':
#     main()
