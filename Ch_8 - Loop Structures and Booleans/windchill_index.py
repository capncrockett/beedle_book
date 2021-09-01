# # windchill_index.py
#
# temps_list = []
# wind_speed_list = []
#
# for temps in range(-20, 61, 10):
#     temps_list.append(temps)
#
# for wind_speeds in range(0, 51, 5):
#     wind_speed_list.append(wind_speeds)
#
# # print columns header
# for i in range(len(temps_list)):
#     print(f"{temps_list[i]:5.0f}", end="")
#
# print()
#
# # print rows
# for i in range(len(temps_list)):
#     wind_speed = wind_speed_list[i]
#     print(f"{wind_speed:2.0f} ", end="")
#
#     for x in range(len(temps_list)):
#         temp = temps_list[x]
#
#         windchill_index = 35.74 \
#                           + 0.6125 * temp \
#                           - 35.75 * (wind_speed ** 0.16) \
#                           + 0.4275 * temp * (wind_speed ** 0.16)
#         print(f"{windchill_index:3.1f} ", end="")
#     print()


# c08ex02.py
#   Windchill Table

def windChill(t, v):
    if v > 3:
        chill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
    else:
        chill = t
    return chill

def main():

    # Print table headings
    print("Wind Chill Table\n\n")
    print("Temperature".center(70))
    print("MPH|", end=' ')
    temps = list(range(-20,61,10))
    for t in temps:
        print("{0:5}".format(t), end=' ')
    print("\n---+" + 55 * '-')

    # Print lines in table
    for vel in range(0,51,5):
        print("{0:3}|".format(vel), end=' ')
        for temp in temps:
            print("{0:5.0f}".format(windChill(temp, vel)), end=' ')
        print()
    print()

main()