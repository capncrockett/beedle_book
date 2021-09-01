heating = 0.0
cooling = 0.0

temp = -10

heating = heating + max(0, 60-temp)
cooling = cooling + max(0, temp-80)

print(max(0, 60))


# def monthsrequiredfordownpaymentt(annual_salary, portion_saved, total_cost, semi_annual_raise):
#     month = 0
#     current_savings = 0
#     portion_down_payment = 0.25
#     r = 0.04
#     monthly_salary = float(annual_salary / 12)
#     print(monthly_salary)
#     newtotalcost = float(total_cost * portion_down_payment)
#     print(newtotalcost)
#     while current_savings < newtotalcost:
#         month += 1
#         investment = current_savings * r / 12
#         current_savings += float(investment)
#         if month % 6 == 0:
#             annual_salary += annual_salary * semi_annual_raise
#             monthly_salary = annual_salary / 12
#             portiontobesaved = monthly_salary * portion_saved
#         else:
#             portiontobesaved = monthly_salary * portion_saved
#         current_savings = current_savings + portiontobesaved
#     return month
#
#
# print(monthsrequiredfordownpaymentt(36000, 1000, 310000, 200))
#
#

# # create and test multiply() function
#
# def multiply(str_1, str_2):
#     str_1 = int(input("Enter the first number to multiply: "))
#     str_2 = int(input("Enter the second number to multiply: "))
#     product = str_1 * str_2
#     return str(product)
#
#
# print(multiply('x', 'y'))
#
# some_list = [1, 3, 5]
# x = 6
#
# for nums_1 in some_list:
#     for nums_2 in some_list:
#         if nums_1 + nums_2 == x:
#             print(nums_1, nums_2)
#         else:
#             break
