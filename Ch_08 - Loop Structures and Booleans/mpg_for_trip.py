# mpg_for_trip.py

def mpg(m, g) -> float:
    mileage = m / g
    return round(mileage, 1)


def main():
    print("This program calculates your gas mileage for a multi-leg trip.\n"
          "Enter your odometer reading and gas usage separated by a \n"
          "comma. When finished just hit <ENTER>.")
    print()

    # set odometer and fuel
    distance, fuel = [], [0]
    init_odometer = float(input("Enter initial odometer reading: "))
    distance.append(init_odometer)

    # First leg entry
    data_str = input("Enter odometer and gallons (with a comma between): ")

    # Get user info for legs of the trip
    while data_str != "":
        inputs = data_str.split(",")
        odometer, gallons = float(inputs[0]), float(inputs[1])
        distance.append(odometer)
        fuel.append(gallons)
        trip_miles = odometer - distance[-2]
        print(f"MPG for this leg: {mpg(trip_miles, gallons)}")

        # Get next leg or quit with blank entry
        data_str = input("Enter odometer and gallons (with a comma "
                         "between: ")

    print()
    trip_total = (distance[-1]) - init_odometer
    fuel_total = sum(fuel)
    print(f"You traveled a total of {trip_total} miles on {fuel_total} gallons.")
    print(f"You averaged {mpg(trip_total, fuel_total)} miles per gallon.")


if __name__ == '__main__':
    main()
