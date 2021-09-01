# syracuse_sequence.py

def syracuse(x):
    count = 0
    init_x = x
    while x != 1:
        if x % 2 == 0:
            print(f"{x}/2", end="")
            x = x // 2
            print(f" = {x}")
            count = count + 1
        elif x % 2 != 0:
            print(f"3 * {x} + 1", end="")
            x = 3 * x + 1
            print(f" = {x}")
            count = count + 1

    # If running single user input.
    print(f"It would take {count:0.0f} iterations to reduce "
          f"{init_x:0.0f} to 1.")

    # If running max iterations.
    # print(f"It would take {count:4.0f} iterations to reduce "
    #       f"{init_x:0.0f} to 1.")

    return count


def main():
    print("This program runs a number through the Syracuse sequence.\n")
    x = int(input("Please enter a number >> "))
    syracuse(x)

    # If you want to run multiple instances an find the highest amount
    # of iterations necessary to reduce to 1.

    # iterations = []
    # for i in range(1, 100):
    #     iterations.append(syracuse(i))
    # highest_iter = max(iterations)
    # print(f"Highest amount of iterations = {highest_iter}")


main()
