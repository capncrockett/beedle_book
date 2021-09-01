# cannonboru_2.py
import math
from math import cos, sin


def get_inputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input(
        "Enter the time interval between position calculations: "))

    return a, v, h, t


def get_xy_components(vel, angle):
    # convert angle to radians
    theta = math.radians(angle)
    x_vel = vel * cos(theta)
    y_vel = vel * sin(theta)

    return x_vel, y_vel


def update_cannonball(time, x_pos, y_pos, x_vel, y_vel):
    x_pos = x_pos + time * x_vel
    y_vel_1 = y_vel - time * 9.8
    y_pos = y_pos + time * (y_vel + y_vel_1) / 2
    y_vel = y_vel_1

    return x_pos, y_pos, y_vel


def main():
    angle, vel, h0, time = get_inputs()

    # set the initial position and velocities in x and y directions.
    x_pos, y_pos = 0.0, h0
    x_vel, y_vel = get_xy_components(vel, angle)

    # loop until the ball hits the ground
    while y_pos >= 0:
        # calculate position and velocity in time seconds
        x_pos, y_pos, y_vel = update_cannonball(time, x_pos, y_pos, x_vel, y_vel)
        print(f"D = {x_pos:0.1f}, H = {y_pos:0.1f}")

    print(f"\nDistance traveled: {x_pos:0.1f} meters")


if __name__ == '__main__':
    main()
