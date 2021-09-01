import math

# # 3.a
# total = 0.0
# count = 1
# n = 5
# while count <= n:
#     total = total + count
#     count = count + 1
#
# print(f"The sum of the first {n} numbers is equal to {total}")


# total = 0.0
# count = 1
# n = 5
# while count < 2 * n:
#     total = total + count
#     count = count + 2
#
# print(f"The sum of the first {n} odd numbers is {total}")

# total = 0.0
# x = input("Enter a number to add (999 to quit) >> ")
# while x != 999:
#     total = total + x
#     x = input("Enter a number to add (999 to quit) >> ")
#
# print(f"Total = {total}")

count = 0
n = 10
while n > 1:
    n = n / 2
    count = count + 1

print(f"{n} can be divided by 2: {count} times.")
print(math.log2(10))

