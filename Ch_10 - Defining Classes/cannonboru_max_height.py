# cannonboru_max_height.py
from projectile import Projectile


def get_inputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input(
        "Enter the time interval between position calculations: "))

    return a, v, h, t


def main():
    angle, vel, h0, time = get_inputs()
    cball = Projectile(angle, vel, h0)
    max_height = h0

    # loop until the ball hits the ground
    while cball.get_y() >= 0:
        cball.update(time)
        if cball.get_y() > max_height:
            max_height = cball.get_y()
        print(f"D = {cball.get_x():0.1f}, H = {cball.get_y():0.1f}")

    print(f"\nDistance traveled: {cball.get_x():0.1f} meters")
    print(f"Max height: {max_height:0.1f} meters")


if __name__ == '__main__':
    main()
