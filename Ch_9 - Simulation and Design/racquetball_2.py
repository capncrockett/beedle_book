# racquetball_2.py
#   A program to simulate win probability for a series of racquetball
#   matches.
from racquetball_1 import *


def print_intro():
    print('\nThis program simulates a series of racquetball matches \n'
          'between two players called "A" and "B". The skill level \n'
          'of each player is indicated by a probability (between 0 \n'
          'and 1) that the player wins the point when serving. \n'
          'Player A always has the first serve.\n')


def get_inputs():
    # Returns the three simulation parameters prob_a, prob_b, and n.
    a = float(input("What is the probability (0.x) that player A will "
                    "win a serve? "))
    b = float(input("What is the probability (0.x) that player B will "
                    "win a serve? "))
    n = int(input("How many matches should we simulate? "))

    return a, b, n


def sim_n_matches(prob_a, prob_b, n):
    # Initialize match wins to 0
    match_win_a = 0
    match_win_b = 0
    games = 0

    for i in range(n):
        win_a, win_b = sim_one_match(prob_a, prob_b)
        if win_a > win_b:
            match_win_a = match_win_a + 1
        else:
            match_win_b = match_win_b + 1

        games = games + (win_a + win_b)

    return match_win_a, match_win_b, games


def sim_one_match(prob_a, prob_b):
    # Initialize game wins to 0
    wins_a = 0
    wins_b = 0

    for i in range(5):
        while not match_over(wins_a, wins_b):
            score_a, score_b = sim_one_game(prob_a, prob_b)
            if score_a > score_b:
                wins_a = wins_a + 1
            else:
                wins_b = wins_b + 1
        break

    return wins_a, wins_b


def match_over(a, b):
    # a and b represent win totals for a racquetball match
    # Returns True if the match is over, False otherwise
    return a == 3 or b == 3


def print_summary(wins_a, wins_b, games):
    # Prints a summary of wins for each player.
    matches = wins_a + wins_b
    print(f"\nMatches Simulated: {matches}")
    print(f"Games Simulated: {games}")
    print(f"Match Wins for A: {wins_a} {(wins_a / matches):0.1%}")
    print(f"Match Wins for B: {wins_b} {(wins_b / matches):0.1%}%")


def main():
    print_intro()

    # for i in range(10):

    # Get probabilities and desired match sim total.
    prob_a, prob_b, n = get_inputs()

    # Simulate n matches of racquetball (best 3 out of 5)
    match_wins_a, match_wins_b, total_games = sim_n_matches(prob_a, prob_b, n)

    # Print a report on the wins for player_a and player_b.
    print_summary(match_wins_a, match_wins_b, total_games)
    print()


if __name__ == '__main__':
    main()
