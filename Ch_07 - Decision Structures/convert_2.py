# convert_2.py
#   A program to convert Celsius temps to Fahrenheit.
#   This version issues heat and cold warnings.

def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print(f"The temperature is {fahrenheit} degrees fahrenheit.")

    # Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrr. Be sure to dress warmly!")


main()
