# racquetball_1.py
#   A program to simulate win probability for a series of racquetball
#   games.
from random import random


def print_intro():
    print('\nThis program simulates a game of racquetball between two \n'
          'players called "A" and "B". The skill level of each player \n'
          'is indicated by a probability (between 0 and 1) that the  \n'
          'player wins the point when serving. Player A always has \n'
          'the first serve.\n')


def get_inputs():
    # Returns the three simulation parameters prob_a, prob_b, and n.
    a = float(input("What is the probability (0.x) that player A will "
                    "win a serve? "))
    b = float(input("What is the probability (0.x) that player B will "
                    "win a serve? "))
    n = int(input("How many games should we simulate? "))
    return a, b, n


def sim_n_games(prob_a, prob_b, n):
    # Initialize wins_a and wins_b to 0
    wins_a = 0
    wins_b = 0

    # loop n times
    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1
    return wins_a, wins_b


def sim_one_game(prob_a, prob_b):
    # Initialize scores to 0
    score_a = 0
    score_b = 0

    # Set serving to "A"
    serving = "A"

    # Loop while game is not over:
    while not game_over(score_a, score_b):
        # Simulate one serve of whichever player is serving
        if serving == "A":
            if random() < prob_a:       # A wins the serve
                score_a += 1
            else:
                serving = "B"           # A loses the serve
        else:
            if random() < prob_b:       # B wins the serve
                score_b += 1
            else:
                serving = "A"          # B loses the serve

    return score_a, score_b


def game_over(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise
    return a == 15 or b == 15


def print_summary(wins_a, wins_b):
    # Prints a summary of wins for each player.
    n = wins_a + wins_b
    print(f"\nGames Simulated: {n}")
    print(f"Wins for A: {wins_a} {(wins_a / n):0.1%}")
    print(f"Wins for B: {wins_b} {(wins_b / n):0.1%}%")


def main():
    print_intro()

    # for i in range(10):

    # Get probabilities and desired game sim total.
    prob_a, prob_b, n = get_inputs()

    # Simulate n games of racquetball using prob_a and prob_b.
    wins_a, wins_b = sim_n_games(prob_a, prob_b, n)

    # Print a report on the wins for player_a and player_b.
    print_summary(wins_a, wins_b)
    print()


if __name__ == '__main__':
    main()
