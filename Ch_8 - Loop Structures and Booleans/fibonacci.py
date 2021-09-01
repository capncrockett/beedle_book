# fibonacci.py
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
#
# last_num = 0
# this_num = 1
# n = int(input("What number in the fibonacci sequence are we after? "))
# for i in range(n - 1):
#     next_num = last_num + this_num
#     this_num = last_num
#     last_num = next_num
#
# print(this_num)


fib_list = [0, 1]

n = int(input("What number in the fibonacci sequence are we after? "))
while len(fib_list) != n:
    next_num = fib_list[-1] + fib_list[-2]
    fib_list.append(next_num)
    print(next_num)
print(fib_list)

print(f"The last two numbers are "
      f"{fib_list[-2]} and {fib_list[-1]}.")
