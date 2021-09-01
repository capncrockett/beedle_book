# chaos_better.py
#   A simple program illustrating chaotic behavior in a cleaner table.


def main():
    print("This program illustrates a chaotic function")
    print()

    x1, x2 = eval(input("Enter two numbers between 0 and 1 "
                        "separated by a comma: "))
    n = eval(input("How many times should I run the numbers? "))
    # x1, x2, n = 0.2, 0.7, 11  FOR TESTING

    print(f"index {x1:^10.2f} {x2:^10.2f}")
    print("-" * 26)
    for i in range(n):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{0:>5} {1:^10.6f} {2:^10.6f}".format(i, x1, x2))


main()
