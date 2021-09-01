# factorial.py
#   Program to compute the factorial of a number.
#   Illustrates for loop with an accumulator.

def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact *= factor
    print("The factorial of", n, "is", fact)


main()
# print(-10 // 3)
# print(-10 % 3)
# print(10 // -3)
# print(10 % -3)
# print(-10 // -3)
#
# print(abs(4 - 20 // 3) ** 3)
# print(20 // 3)  # 6
