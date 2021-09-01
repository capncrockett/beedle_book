# congress_recs.py
#   A program to check US senator and State Rep eligibility.

def residency_requirement(years: int):
    state_rep = 7
    senator = 9
    if years < state_rep:
        print(f"{years} years does not meet residency requirements.\n"
              f"State Rep = {state_rep} years.\n"
              f"Senator = {senator} years.")
    elif state_rep <= years < senator:
        print(f"{years} years meets residency requirements for "
              f"State Rep!\n"
              f"Senator = {senator} years")
    else:
        print("You meet all residency requirements to be a State Rep "
              "or a Senator!")


def age_requirements(years: int):
    state_rep = 25
    senator = 30
    if years < state_rep:
        print(f"{years} years old does not meet the age requirements.\n"
              f"State Rep = age {state_rep}.\n"
              f"Senator = age {senator}.")
    elif state_rep <= years < senator:
        print(f"{years} years old meets age requirements for State "
              f"Rep!\n "
              f"Senator = age {senator}.")
    else:
        print("You meet all age requirements to be a State Rep or a "
              "Senator!")


def main():
    age = int(input("Please enter your age: "))
    residency = int(input("How long have you lived in the U.S.? "))
    print()

    age_requirements(age)
    print()
    residency_requirement(residency)


main()

# # c07ex08.py
# #   Eligibility for Congress
# #   Note: This solution does not use Boolean operators, since
# #         they are introduced in Chapter 8.
#
# def main():
#     print("Congressional Eligibility\n")
#     age = int(input("Enter your age: "))
#     residency = int(input("Enter years of residency: "))
#     if age >= 30:
#         if residency >= 9:
#             print("You are eligible for the Senate and the House.")
#         elif residency >= 7:
#             print("You are eligible only for the House.")
#         else:
#             print("You are not eligible for Congress.")
#     elif age >= 25:
#         if residency >= 7:
#             print("You are eligible only for the House.")
#         else:
#             print("You are not eligible for Congress.")
#     else:
#         print("You are not eligible for Congress.")
#
#
# if __name__ == '__main__':
#     main()
