# volleyball_compare.py
#   A program to investigate potential advantage for rally scoring or
#   standard scoring in a series of volleyball games.
from volleyball_1 import *


def print_intro():
    print("\nThis program simulates volleyball games in an effort to \n"
          "investigate whether rally scoring magnifies, reduces, or \n"
          "has no effect on the relative advantage enjoyed by the \n"
          "better of two teams. Team A always serves first.\n")


def get_inputs():
    # Returns the three simulation parameters prob_a, prob_b, n,
    a = float(input("What is the probability (0.x) that team A will "
                    "win a serve? "))
    b = float(input("What is the probability (0.x) that team B will "
                    "win a serve? "))
    n = int(input("How many games should we simulate for each system? "))

    return a, b, n


def sim_n_stnd_games(a, b, n):
    # set wins to 0
    wins_a = wins_b = 0

    for i in range(n):
        score_a, score_b = sim_one_game(a, b, 0)   # 0 indicates standard scoring
        if score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1

    return wins_a, wins_b


def sim_n_rally_games(a, b, n):
    # set wins to 0
    wins_a = wins_b = 0

    for i in range(n):
        score_a, score_b = sim_one_game(a, b, 1)   # 1 indicates rally scoring
        if score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1

    return wins_a, wins_b


def print_comp_summary(std_w_a, std_w_b, rly_w_a, rly_w_b):
    std_games = std_w_a + std_w_b
    rly_games = rly_w_a + rly_w_b
    total_games = std_games + rly_games
    total_wins_a = std_w_a + rly_w_a
    total_wins_b = std_w_b + rly_w_b

    print(f"\n |Team A|\n"
          f"Standard Wins: {std_w_a} {std_w_a / std_games:0.1%}\n"
          f"   Rally Wins: {rly_w_a} {rly_w_a / rly_games:0.1%}\n"
          f"   Total Wins: {total_wins_a} {total_wins_a / total_games:0.1%}\n"
          
          f"\n |Team B|\n"
          f"Standard Wins: {std_w_b} {std_w_b / std_games:0.1%}\n"
          f"   Rally Wins: {rly_w_b} {rly_w_b / rly_games:0.1%}\n"
          f"   Total Wins: {total_wins_b} {total_wins_b / total_games:0.1%}\n")


def main():
    print_intro()

    # INPUT: Win probabilities for both teams. How many games to sim.
    prob_a, prob_b, n = get_inputs()

    # Simulate n games for both standard and rally using given probs.
    std_wins_a, std_wins_b = sim_n_stnd_games(prob_a, prob_b, n)
    rly_wins_a, rly_wins_b = sim_n_rally_games(prob_a, prob_b, n)

    # OUTPUT: Print a nice summary detailing wins for both teams using
    # both scoring systems.
    print_comp_summary(std_wins_a, std_wins_b, rly_wins_a, rly_wins_b)


if __name__ == '__main__':
    main()
