# volleyball_1.py
#   A program that simulates a game of volleyball.
from random import random


def print_intro():
    print("This program simulates a game of volleyball between teams \n"
          "A and B. A volley win probability must be given for each \n"
          "team. Team A always serves first.")


def get_inputs():
    # Returns the four simulation parameters prob_a, prob_b, and n,
    # scoring.
    s = int(input("Choose scoring system: "
                  "0 for Standard, 1 for Rally"))
    a = float(input("What is the probability (0.x) that team A will "
                    "win a serve? "))
    b = float(input("What is the probability (0.x) that team B will "
                    "win a serve? "))
    # n = int(input("How many matches should we simulate? "))

    return a, b, s


def sim_one_game(prob_a, prob_b, scoring):
    # set service to Team A and scores to 0
    serving = "A"
    score_a = score_b = 0

    # STANDARD SCORING
    if scoring == 0:
        while not game_over_standard(score_a, score_b):
            if serving == "A":
                if random() < prob_a:
                    score_a = score_a + 1
                else:
                    serving = "B"
            else:
                if random() < prob_b:
                    score_b = score_b + 1
                else:
                    serving = "A"

        return score_a, score_b

    # RALLY SCORING
    else:
        while not game_over_rally(score_a, score_b):
            if serving == "A":
                if random() < prob_a:
                    score_a = score_a + 1
                else:
                    score_b = score_b + 1
                    serving = "B"
            else:
                if random() < prob_b:
                    score_b = score_b + 1
                else:
                    score_a = score_a + 1
                    serving = "A"

        return score_a, score_b


def game_over_standard(a, b):
    # a and b represent two scores for a volleyball game. Returns True
    # if the game is over. False otherwise.
    return ((a >= 15 and (a - b) >= 2) or
            (b >= 15 and (b - a) >= 2))


def game_over_rally(a, b):
    # a and b represent two scores for a volleyball game. Returns True
    # if the game is over. False otherwise.
    return ((a >= 25 and (a - b) >= 2) or
            (b >= 25 and (b - a) >= 2))


def print_summary(score_a, score_b):
    if score_a > score_b:
        team = "A"
    else:
        team = "B"

    print(f"Team {team} wins with a score of {score_a} to {score_b}.")


def main():
    # print an intro about volleyball
    print_intro()

    # INPUT: win prob for team A and B, how many games to sim.
    prob_a, prob_b, scoring = get_inputs()

    # simulate a game: can only score when serving. Service alternates.
    score_a, score_b = sim_one_game(prob_a, prob_b, scoring)

    # OUTPUT: print a summary of the results. Games simmed. Wins for A and B
    print_summary(score_a, score_b)


if __name__ == '__main__':
    main()
