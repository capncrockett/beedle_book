# babysitter_calc.py
# A program to calculate pay for a babysitter.

def main():
    print("Babysitting Calculator")
    print("Enter times in 24 hour format (e.g. 8pm = 20:00)")
    start_hrs, start_min = input("Enter start time: ").split(":")
    end_hrs, end_min = input("Enter end time: ").split(":")

    start = int(start_hrs) + float(start_min) / 60
    end = int(end_hrs) + float(end_min) / 60

    # Correct for midnight rollover
    if end < start:
        end = end + 24

    bedtime = 21

    # Rates
    prime_rate = 2.5
    extra_rate = 1.75

    # Totals
    prime_hrs = 0
    extra_hrs = 0

    if start < bedtime:
        if end < bedtime:                           # Early night
            prime_hrs = end - start
        else:                                       # Normal night
            prime_hrs = bedtime - start
            extra_hrs = end - bedtime
    else:                                           # Late start
        extra_hrs = end - start

    prime_total = prime_hrs * prime_rate
    extra_total = extra_hrs * extra_rate

    print(f"\nPrime hrs = {prime_hrs}\n"
          f"Prime total: ${prime_total:0.02f}\n"
          f"Extra hrs = {extra_hrs}\n"
          f"Extra total: ${extra_total:0.02f}\n"
          f"Grand total: ${prime_total + extra_total:0.02f}")


if __name__ == '__main__':
    main()


# # c07ex07.py
# #    Babysitter pay
# #    This is a subtle problem with many possible solutions
#
#
# def main():
#     print("Babysitting Calculator\n")
#     print("Enter times using 24 hour format (e.g. 8 pm is 20:00)")
#     s_hours, s_mins = input("Starting time (hh:mm): ").split(":")
#     e_hours, e_mins = input("Ending time (hh:mm): ").split(":")
#
#     # convert to hours since midnight
#     start = int(s_hours) + float(s_mins)/60.0
#     end = int(e_hours) + float(e_mins)/60.0
#
#     if end < start:     # correct for rollover at midnight
#         end = end + 24
#
#     bedtime = 21.0
#     # calculate pre and post bedtime hours
#     if start < bedtime:
#         if end < bedtime:
#             prime_hours = end - start
#             extra_hours = 0.0
#         else:
#             prime_hours = bedtime - start
#             extra_hours = end - bedtime
#     else:
#         prime_hours = 0.0
#         extra_hours = end - start
#
#     pay = 2.50 * prime_hours + 1.75 * extra_hours
#     print("Total payment due: ${0:0.2f}".format(pay))
#
#
# if __name__ == '__main__':
#     main()
