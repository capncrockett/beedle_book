# racquetball_3.py
#   A program to simulate win probability for a series of racquetball
#   matches. Service alternates: A serves odd games in odd matches. B
#   serves even games in even matches.
from racquetball_1 import *
from racquetball_2 import *



def sim_one_game_alternate(prob_a, prob_b, serve):
    # Initialize scores to 0
    score_a = 0
    score_b = 0

    # Set serving to "A"
    serving = serve

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


def sim_one_match_alternate(prob_a, prob_b):
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
