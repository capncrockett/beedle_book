# def sum_diff(x, y):
#     sum = x + y
#     diff = x - y
#     return sum, diff
#
#
# num_1, num_2 = input("Please enter two numbers (x, y): ").split(",")
# s, d = sum_diff(float(num_1), float(num_2))
# print(f"The sum is {s} and the difference is {d}. Thanks for playing.")

def test_print():
    print("test one " * 2)


def test_return():
    return "test return"


test_print()            # "test one".
print("***")
test_return()           # nothing. Not even a blank line.
print("***")
print(test_print())     # "test one" AND None type.
print("***")
print(test_return())    # "test return".
print("***")
