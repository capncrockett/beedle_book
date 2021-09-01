# def main():
#     print("This program converts Celsius to Fahrenheit.")
#     for celsius in range(5):
#         celsius = eval(input("What is the Celsius temperature? "))
#         fahrenheit = 9 / 5 * celsius + 32
#         print("The temperature is", fahrenheit, "degrees Fahrenheit.")
#         # input("Press the <Enter> key to quit.")
#
#
# main()
#
# def main():
#     for celsius in range(0, 101, 10):  # start, stop, by.
#         fahrenheit = 9 / 5 * celsius + 32
#         print(celsius, fahrenheit)
#
def main():
    # print("This program converts Celsius to Fahrenheit.")
    # for celsius in range(5):
    #     celsius = eval(input("What is the Celsius temperature? "))
    #     fahrenheit = 9 / 5 * celsius + 32
    #     print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    #     input("Press the <Enter> key to quit.")

    print("This program converts Fahrenheit to Celsius.")
    for fahrenheit in range(5):
        fahrenheit = eval(input("What is the Fahrenheit temperature? "))
        celsius = (5 * fahrenheit - 160) / 9
        print("The temperature is ", celsius, "degrees Celsius.")
        print()


main()
