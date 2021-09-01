# ch_9_notes.py
# from random import randrange, random, randint, uniform

# import numpy as np

# random_float_array = np.random.uniform(75.5, 125.5, size=(20, 3))
# print(random_float_array)


# for i in range(25):
#     print(randrange(11))
#     # OR
#     print(randint(0, 11))
#
#     print(random() - 0.5)
#     # OR
#     print(uniform(-0.5, 0.5))
#
#     d6_1 = randrange(1, 7)
#     d6_2 = randrange(1, 7)
#     print(f"First die = {d6_1}")
#     print(f"Second die = {d6_2}")
#     print(f"Total roll = {d6_1 + d6_2}")
#
#     print(random() * 20 - 10.0)
#     # OR
#     print(uniform(-10.0, 10))
#
#     print("*********************")

# INPUT: The program first prompts for an gets the service
#        probabilities of the two players (called "player A" and
#        "player B". Then the program prompts for and gets the number
#        of games to be simulated.

# OUTPUT: The program will provide a series of initial prompts such as
#         the following:
# What is the prob. player A wins a serve?
# What is the prob. player B wins a serve?
# How many games to simulate?

# The program will print out a nicely formatted report showing the
# number of games simulated and the number of wins and winning
# percentage for each player. Example:

# Games Simulated : 500
# Wins for A: 268 (53.6%)
# Wins for B: 232 (46.4%)

# NOTES: All inputs are assumed to be legal numeric values; no error or
#        validity checking is required.
#        In each simulated game, player A serves first.


# def main():
# print_intro()
# prob_a, prob_b, n = get_inputs()
# wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
# print_summary(wins_a, wins_b)


# rate_list = []
# for i in range(100):
#     i = sim()
#     rate_list.append(i)
# print(rate_list)


# def sim(prob, games):
#     wins = 0
#     losses = 0
#     # games = 350
#     # prob = 0.7
#     for i in range(games):
#         if random() < (prob * 0.01):
#             wins += 1
#         else:
#             losses += 1
#     win_rate = round((wins / games) * 100, 1)
#
#     # print(f"Wins: {wins}, Losses: {losses}")
#     # print(f"Win rate: {win_rate}%")
#     return wins, losses, win_rate
#
#
# atk_tot = 5
# def_tot = 4
#
# while def_tot != 0:
#     valid_inputs = ['1', '2', '3', 'B', 'b', 'R', 'r']
#     action = str(input("How would you like to proceed? \n"
#                        "Enter 1, 2, or 3 to roll corresponding "
#                        "amount of dice.\n"
#                        "B for blitz mode.\n"
#                        "R to retreat\n"))
#     if action not in valid_inputs:
#         print("Invalid Input. Try Again.\n")
#         continue
#     else:
#         print(f"You chose {action}\n")
#
# print(atk_tot, def_tot)
#
# from risk_battle import d6
#
# atk_dice = 1
# def_dice = 1
#
# atk_rolls = []
# def_rolls = []
#
# for dice in range(atk_dice):
#     atk_rolls.append(d6())
# for dice in range(def_dice):
#     def_rolls.append(d6())
#
# print(f"Attack: {atk_rolls}")
# print(f"Defend: {def_rolls}")
#
# if atk_dice > 1:
#     atk_rolls.remove(min(atk_rolls))
# else:
#     print(f"Attack: {atk_rolls}")
#     print(f"Defend: {def_rolls}")
#
#     atk_wins = 0
#     def_wins = 0
#
#     for i in range(len(def_rolls)):
#         if max(atk_rolls) > max(def_rolls):
#             atk_wins = atk_wins + 1
#         else:
#             def_wins = def_wins + 1
#         atk_rolls.remove(max(atk_rolls))
#         def_rolls.remove(max(def_rolls))
#
#     print(f"A wins: {atk_wins}")
#     print(f"D wins: {def_wins}")
