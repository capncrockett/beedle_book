# cannonboru_1.py
import math
from math import cos, sin


def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    init_height = float(input("Enter the initial height (in meters): "))
    time = float(input(
        "Enter the time interval between position calculations: "))

    # convert angle to radians
    theta = math.radians(angle)

    # set the initial position and velocities in x and y directions.
    x_pos = 0.0
    y_pos = init_height
    x_vel = vel * cos(theta)
    y_vel = vel * sin(theta)

    # loop until the ball hits the ground
    while y_pos >= 0.0:
        # calculate position and velocity in time seconds
        x_pos = x_pos + time * x_vel
        y_vel_1 = y_vel - time * 9.8
        y_pos = y_pos + time * (y_vel + y_vel_1) / 2
        y_vel = y_vel_1
        print(f"D = {x_pos:0.1f}, H = {y_pos:0.1f}")

    print(f"\nDistance traveled: {x_pos:0.1f} meters")


if __name__ == '__main__':
    main()
