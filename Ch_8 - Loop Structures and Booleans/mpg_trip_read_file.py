# mpg_trip_read_file.py

def mpg(m, g) -> float:
    mileage = m / g
    return round(mileage, 1)


def main():
    print("This program calculates your gas mileage for a multi-leg \n"
          "trip from a text file.\n")
    # infile = open(input("What file is the trip data in? "), "r")
    infile = open("trip data.txt")

    # set odometer and fuel
    distance, fuel = [], [0]
    init_odometer = float(infile.readline())
    distance.append(init_odometer)

    # First leg entry
    data_str = infile.readline()

    # Get user info for legs of the trip
    while data_str != "":
        inputs = data_str.split(",")
        odometer, gallons = float(inputs[0]), float(inputs[1])
        distance.append(odometer)
        fuel.append(gallons)
        trip_miles = odometer - distance[-2]
        print(f"MPG for this leg: {mpg(trip_miles, gallons)}")

        # Get next leg or quit on empty line
        data_str = infile.readline()

    print()
    trip_total = (distance[-1]) - init_odometer
    fuel_total = round(sum(fuel), 1)
    print(f"You traveled a total of {trip_total} miles on {fuel_total} gallons.")
    print(f"You averaged {mpg(trip_total, fuel_total)} miles per gallon.")


if __name__ == '__main__':
    main()
