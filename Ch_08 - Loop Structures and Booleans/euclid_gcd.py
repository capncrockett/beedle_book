# c08ex08.py
#    Euclid's algorithm for GCD

def gcd(m, n):
    while m != 0:
        # will do the changeover at the same time. Muy importante.
        n, m = m, n % m

        # will NOT do the changeover at the same time :(
        # n = m
        # m = n % m
    return n


def main():
    print("Euclid's GCD algorithm\n")
    x_1, x_2 = input("Enter two natural numbers (n1, n2): ").split(", ")
    # x_1, x_2 = 270, 192     # FOR TESTING
    print(f"The GCD of {x_1} and {x_2} is {gcd(int(x_1), int(x_2))}")


if __name__ == '__main__':
    main()


# # euclid_gcd.py
# #   Finds the greatest common denominator using Euclid's algorithm.
#
# print("Euclid's Algorithm for finding the greatest common denominator.\n")
#
# # input: two numbers (m, n)
# # m = int(input("Enter a whole positive number"))
# # n = int(input("Enter a second whole positive number"))
# curr_m = 270
# curr_n = 192
#
# while curr_m % curr_n != 0:
#     new_n = curr_m % curr_n
#     new_m = curr_n
#     print(new_m, new_n)
#     curr_m = new_m
#     curr_n = new_n
#
#     if curr_m % curr_n == 0:
#         print(f"The GCD is {curr_n}")
