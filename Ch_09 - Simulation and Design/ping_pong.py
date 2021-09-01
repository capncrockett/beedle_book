# ping_pong.py
#   A program to simulate a ping pong game.
from random import random
from random import randrange


def print_intro():
    print("Ping pong simulator.")


def get_inputs():
    a = float(input("Probability that player A wins a serve (0.x): "))
    b = float(input("Probability that player B wins a serve (0.x): "))
    # n = int(input("How many games should simulate? "))
    return a, b


def sim_one_game(prob_a, prob_b):
    score_a = score_b = 0
    serving = randrange(1)  # Sets service to random

    while not game_over(score_a, score_b):
        # simulate two serves
        if serving == 0:                    # 0 = A serving
            for serves in range(1):         # two serves per player
                if random() < prob_a:
                    score_a = score_a + 1   # A wins serve
                else:
                    score_b = score_b + 1   # B wins serve
            serving = 1

        else:                               # 1 = B serving
            for serves in range(1):         # two serves per player
                if random() < prob_b:
                    score_b = score_b + 1   # B wins serve
                else:
                    score_a = score_a + 1   # A wins serve
            serving = 0

    return score_a, score_b


def game_over(a, b):
    return ((a >= 11 and (a - b) >= 2) or
            (b >= 11 and (b - a) >= 2))


def print_summary(score_a, score_b):
    print(f"\nA: {score_a} | B: {score_b}")


def main():
    print_intro()
    prob_a, prob_b = get_inputs()
    score_a, score_b = sim_one_game(prob_a, prob_b)
    print_summary(score_a, score_b)


for i in range(10):
    main()
