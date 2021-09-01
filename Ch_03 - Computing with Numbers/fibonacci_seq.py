# fibonacci.py
#   A program to determine the value a number in the Fibonacci sequence.

def main():
    print("This program computes the 'nth' number in the Fibonacci "
          "sequence.")
    n = int(input("Enter a value for n: "))

    curr, prev = 1, 1

    for i in range(n - 2):
        curr, prev = curr + prev, curr
    print(curr)


main()
