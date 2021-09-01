# racquetball_shutouts.py
#   Racquetball simulation that takes into account shutouts.

# racquetball_2.py
#   A program to simulate win probability for a series of racquetball
#   matches.
from racquetball_1 import *
from racquetball_2 import *


def print_intro():
    print('\nThis program simulates a series of racquetball games \n'
          'between two players called "A" and "B". The skill level \n'
          'of each player is indicated by a probability (between 0 \n'
          'and 1) that the player wins the point when serving. \n'
          'First serve alternates each game.\n')


def get_inputs():
    # Returns the three simulation parameters prob_a, prob_b, and n.
    a = float(input("What is the probability (0.x) that player A will "
                    "win a serve? "))
    b = float(input("What is the probability (0.x) that player B will "
                    "win a serve? "))
    n = int(input("How many matches should we simulate? "))

    return a, b, n


def sim_n_games(prob_a, prob_b, n):
    # Initialize wins_a and wins_b to 0
    wins_a = wins_b = 0
    shutouts_a = shutouts_b = 0

    # loop n times
    for i in range(n):
        if n % 2 == 0:
            server = "A"
        else:
            server = "B"
        score_a, score_b = sim_one_game(prob_a, prob_b, server)

        # Check if game was a shutout:
        if score_b == 0:
            shutouts_a = shutouts_a + 1
        elif score_a == 0:
            shutouts_b = shutouts_b + 1

        elif score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1
    return wins_a, wins_b, shutouts_a, shutouts_b


def sim_one_game(prob_a, prob_b, server):
    # Initialize scores to 0
    score_a = score_b = 0

    # Alternate service based on odd or even game.
    serving = server

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
    return ((a == 15 or b == 15) or
            (a == 7 and b == 0) or
            (a == 0 and b == 7))


def print_summary(wins_a, wins_b, shuts_a, shuts_b):
    # Prints a summary of wins for each player.
    total_a_wins = wins_a + shuts_a
    total_b_wins = wins_b + shuts_b
    games = total_a_wins + total_b_wins

    print(f"\nGames Simulated: {games}")
    print(f"Game Wins for A: {total_a_wins} {(total_a_wins / games):0.1%}")
    print(f"Shutouts for A: {shuts_a} {(shuts_a / total_a_wins):0.1%}")

    print(f"\nGame Wins for B: {total_b_wins} {(total_b_wins / games):0.1%}%")
    print(f"Shutouts for B: {shuts_b} {(shuts_b / total_b_wins):0.1%}")


def main():
    print_intro()

    # for i in range(10):

    # Get probabilities and desired game sim total.
    prob_a, prob_b, n = get_inputs()

    # Simulate n games of racquetball
    wins_a, wins_b, shutouts_a, shutouts_b = sim_n_games(prob_a, prob_b, n)

    # Print a report on the wins for player_a and player_b.
    print_summary(wins_a, wins_b, shutouts_a, shutouts_b)
    print()


if __name__ == '__main__':
    main()
