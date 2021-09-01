# risk_battle.py
#   A program to simulate an invasion for the board game RISK.
from random import randrange


def print_intro():
    print("Stuff about stuff")


def get_input():
    """Gets army totals for declared invasion."""
    a = int(input("Total attacking armies? "))
    d = int(input("Total defending armies? "))

    return a, d


def invasion(a, d):
    """Runs an interactive dice rolling sim for RISK.
    Attacking and defending army totals == a and d respectively."""
    atk_tot = a
    def_tot = d

    while def_tot != 0:
        valid_inputs = ['1', '2', '3', 'B', 'b', 'R', 'r']
        action = str(input("\nHow would you like to proceed? \n"
                           "Enter 1, 2, or 3 to roll corresponding "
                           "amount of dice.\n"
                           "B for blitz mode (COMING SOON!).\n"
                           "R to retreat\n"))
        if action not in valid_inputs:
            print("Invalid Input. Try Again.\n")
            continue
        if def_tot == 0:
            break

        else:
            # check defender dice
            if def_tot >= 2:
                def_dice = 2
            else:
                def_dice = 1

            # Roll action TODO write as function
            # TODO message why you can't attack
            if action == '1' and atk_tot > 1:
                a_result, d_result = sim_battle(1, def_dice)
                atk_tot = atk_tot - d_result
                def_tot = def_tot - a_result
            elif action == '2' and atk_tot > 2:
                a_result, d_result = sim_battle(2, def_dice)
                atk_tot = atk_tot - d_result
                def_tot = def_tot - a_result
            elif action == '3' and atk_tot > 3:
                a_result, d_result = sim_battle(3, def_dice)
                atk_tot = atk_tot - d_result
                def_tot = def_tot - a_result

            # # BLITZ MODE! TODO write as a function.
            # elif action == 'B' or action == 'b':
            #     while atk_tot > 1 and def_tot > 0:
            #         if atk_tot == 3:
            #             a_result, d_result = sim_battle(2, def_dice)
            #             atk_tot = atk_tot - d_result
            #             def_tot = def_tot - a_result
            #
            #         if atk_tot == 2:
            #             a_result, d_result = sim_battle(1, def_dice)
            #             atk_tot = atk_tot - d_result
            #             def_tot = def_tot - a_result
            #         else:
            #             a_result, d_result = sim_battle(3, def_dice)
            #             atk_tot = atk_tot - d_result
            #             def_tot = def_tot - a_result

            elif action == 'R' or action == 'r':
                break
        print(f"Atk Armies = {atk_tot}")
        print(f"Def Armies = {def_tot}\n")

        if def_tot == 0:
            print("Invasion successful!")
            break

    # Just in case someone got crushed.
    if atk_tot < 1:
        atk_tot = 1

    return atk_tot, def_tot


def sim_battle(atk_dice, def_dice):
    """Simulates one battle in an invasion. Returns results as lists."""
    # set wins to 0 and empty result lists for dice rolls.
    atk_wins = 0
    def_wins = 0
    atk_rolls = []
    def_rolls = []

    # Roll 'em!
    for dice in range(atk_dice):
        atk_rolls.append(d6())
    for dice in range(def_dice):
        def_rolls.append(d6())

    # Now we know what really happened.
    print(f"\nAttacker: {atk_rolls}")
    print(f"Defender: {def_rolls}\n")

    # Throw out the trash.
    if atk_dice > 1 and def_dice > 0:
        atk_rolls.remove(min(atk_rolls))
    elif atk_dice == 1 and def_dice == 2:
        def_rolls.remove(min(def_rolls))

    # Compare highest pairs. Remove from the equation. Run again
    # if needed.
    for i in range(len(def_rolls)):
        if max(atk_rolls) > max(def_rolls):
            atk_wins = atk_wins + 1
        else:
            def_wins = def_wins + 1

        atk_rolls.remove(max(atk_rolls))
        def_rolls.remove(max(def_rolls))

        # So we know who crushed.
    print(f"A wins: {atk_wins}")
    print(f"D wins: {def_wins}")

    return atk_wins, def_wins


# def sim_blitz(atk_dice, def_dice):
#     """Simulates all battles to the end of invasion."""
#
#     return atk_tot, def_tot


def d6():
    """Returns the roll of a 6-sided die."""
    return randrange(1, 7)


def print_report(atk_tot, def_tot):
    print(f"Attacker: {atk_tot}\n"
          f"Defender: {def_tot}")


def main():
    # Print a nice informative intro
    print_intro()

    # INPUT: invading armies, defending armies.
    atk_init, def_init = get_input()

    # PROCESS: invasion with army totals
    atk_tot, def_tot = invasion(atk_init, def_init)

    # OUTPUT: invasion summary
    print_report(atk_tot, def_tot)


if __name__ == '__main__':
    main()

# for i in range(10):
#     atk_1 = d6()
#     atk_2 = d6()
#     atk_3 = d6()
#     print(atk_1, atk_2, atk_3)
#     print(5 * "*")
