# File: chaos.py
# A simple program illustraing chaotic behavior.

# def main():
#    print("This program illustrates a chaotic function")
#    x = eval(input("Enter a number between 0 and 1: "))
#    for i in range(10):
#        x = 3.9 * x * (1 - x)
#       print(x)
#
# main()

# def main():
#     print("This program illustrates a chaotic function")
#     x = eval(input("Enter a number between 0 and 1: "))
#     n = eval(input("How many numbers should I print? "))
#     for i in range(n):
#         x = 2.0 * x * (1 - x)
#         print(x)
#
# main()
# def main():
#     print("This program illustrates a chaotic function")
#     x = eval(input("Enter a number between 0 and 1: "))
#     for i in range(100):
#         x = 3.9 * x * (1 - x)
#         print(x)
#         x = 3.9 * (x - x * x)
#         print(x)
#         x = 3.9 * x - 3.9 * x * x
#         print(x)
#         print(10 * "-")
#
# main()

# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    x2 = x
    x3 = x
    for i in range(100):
        x = 3.9 * x * (1 - x)
        x2 = 3.9 * (x2 - x2 * x2)
        x3 = 3.9 * x3 - 3.9 * x3 * x3
        print("{:<20} | {:<20} | {:<20}".format(x, x2, x3))

main()