# lightning_distance.py
#   Program to determine the distance to a lightning strike based on
#   elapsed time between the flash and the sound of thunder.

def main():
    print("This program tells you how far away the lightning is.")
    print()

    seconds = int(input("How many seconds until you heard thunder? "))
    distance_feet = 1100 * seconds
    distance_miles = round(distance_feet / 5280, 1)
    print()

    print("The lightning is {} miles, or {} feet, away."
          .format(distance_miles, distance_feet))
    print()
    print("*" * 30)


for i in range(100):
    main()
