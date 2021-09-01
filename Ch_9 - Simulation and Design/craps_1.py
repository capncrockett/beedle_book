# craps_1.py
#   A program that simulates craps.
from risk_battle import d6


def roll_two():
    dice_1, dice_2 = d6(), d6()
    dice_tot = dice_1 + dice_2
    # print(f"{dice_1} + {dice_2} = {dice_tot}")
    return dice_tot


def main():
    win = loss = 0

    for i in range(25):
        natural = [7, 11]
        craps = [2, 3, 12]
        point = [4, 5, 6, 8, 9, 10]

        # Come out roll.
        # print("\nRoll initial")
        init_roll = roll_two()

        # If the roll is 7 or 11 player wins.
        if init_roll in natural:
            # print("Win")
            win += 1
        elif init_roll in craps:
            # print("Lose")
            loss += 1
        # Anything else for initial roll causes player to "roll for point"
        elif init_roll in point:
            # print("Roll for point")

            # Player keeps rolling the dice until either rolling a 7 or re-rolling
            #   the value of the initial roll.
            roll = roll_two()
            while roll != 7 or roll != init_roll:
                # print("Roll again")
                roll = roll_two()
                # If the player re-rolls the initial value before rolling a 7, win.
                if roll == init_roll:
                    # print("Win")
                    win += 1
                    break
                # Rolling a 7 first is a loss.
                elif roll == 7:
                    # print("Lose")
                    loss += 1
                    break
    print(f"Wins = {win}")
    print(f"Loss = {loss}")
    print(f"In playing {i} rounds of craps your odds of winning are {win / i:0.1%}")


if __name__ == '__main__':
    main()
