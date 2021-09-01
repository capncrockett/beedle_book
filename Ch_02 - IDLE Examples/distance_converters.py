#  This program converts distances
def kilometers_miles():

    print("This function converts kilometers to miles.")

    kilometers = eval(input("Enter the distance in kilometers: "))
    miles = kilometers * 0.62
    print("The distance in miles is", miles)


def fahrenheit_kelvin():

    print("This function converts Fahrenheit to Kelvin.")

    fahrenheit = eval(input("Enter the temperature in Fahrenheit: "))
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    print("{} F is equal to {} Kelvin.".format(fahrenheit, kelvin))


fahrenheit_kelvin()
