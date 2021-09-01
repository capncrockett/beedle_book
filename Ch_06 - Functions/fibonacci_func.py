# fibonacci_func.py
#   A function to determine the value a number in the Fibonacci sequence.

def fibonacci(n):
    curr, prev = 1, 1

    for i in range(n - 2):
        curr, prev = curr + prev, curr
    return curr


def main():
    print("This program computes the 'nth' number in the Fibonacci "
          "sequence.")
    n = int(input("Enter a value for n: "))

    print(f"The Fibonacci value is {fibonacci(n)}")


main()
