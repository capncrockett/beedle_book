# speeding_ticket_calc.py
#   A program to calculate the fine for a speeding ticket.

def main():
    speed_limit = eval(input("Enter zone speed limit (mph): "))
    speed = eval(input("Enter speed as (mph): "))
    base_ticket = 50
    five_over = 5
    over_ninety = 200
    fine = round(base_ticket + ((speed - speed_limit) * five_over))

    if speed <= speed_limit:
        print(f"{speed} is under the speed limit of {speed_limit}")
    elif speed > 90:
        total_fine = fine + over_ninety
        print(f"Total fine is ${total_fine} (includes an over-"
              f"90 fine of ${over_ninety})")
    else:
        print(f"Total fine is ${fine}")


main()

# # c07ex06.py
# #    Speeding tickets
#
# def main():
#     print("Speeding fine calculator\n")
#     limit = float(input("Enter the speed limit "))
#     speed = float(input("Enter the clocked speed "))
#
#     if speed <= limit:
#         print("Legal")
#     else:
#         fine = 50 + 5*(speed - limit)
#         if speed > 90:
#             fine = fine + 200
#         print("Fine ${0:0.2f}".format(fine))
#
#
# if __name__ == "__main__":
#     main()
#