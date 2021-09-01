# add_interest_3

def add_interest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)


def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    # You can invoke a function without assigning <var>
    add_interest(amounts, rate)
    print(amounts)


test()


# # addinterest_2
# def add_interest(balance, rate):
#     new_balance = balance * (1 + rate)
#     return new_balance
#
#
# def test():
#     amount = 1000
#     rate = 0.05
#     amount = add_interest(amount, rate)
#     print(amount)
#
#
# test()
#

# # addinterest_1
# def add_interest(balance, rate):
#     new_balance = balance * (1 + rate)
#     balance = new_balance
#
#
# def test():
#     amount = 1000
#     rate = 0.05
#     add_interest(amount, rate)
#     print(amount)
#
#
# test()
