# archery_scorer.py
#   A program that draws an archery target, then lets user click 5
#   "arrows" for points.
from graphics import *
import math


def main():
    win = GraphWin("Archery Game", 600, 600)
    win.setCoords(-6, -6, 6, 6)

    # draw circles with radius' decreasing by 1/5
    radius = 5
    colors = ["white", "black", "blue", "red", "yellow"]
    for circle in colors:
        c1 = Circle(Point(0, 0), radius)
        radius = radius - 1
        c1.setFill(circle)
        c1.draw(win)
        win.setBackground("gray")

    # input: five mouse clicks for the "arrows".
    point_total = 0

    for shots in range(5):
        # Shots fired!
        point = win.getMouse()
        point.draw(win)

        # Calculate distance from center.
        x2 = point.getX()
        y2 = point.getY()
        dx = x2 - 0
        dy = y2 - 0
        dist_from_center = math.sqrt(dx ** 2 + dy ** 2)

        # Tally points
        scoring = [1, 3, 5, 7, 9]

        if dist_from_center < 1:
            print(f"Bulls-eye! {scoring[-1]} points")
            point_total += scoring[-1]

        elif dist_from_center < 2:
            print(f"{colors[-2]}: {scoring[-2]} points")
            point_total += scoring[-2]

        elif dist_from_center < 3:
            print(f"{colors[-3]}: {scoring[-3]} points")
            point_total += scoring[-3]

        elif dist_from_center < 4:
            print(f"{colors[-4]}: {scoring[-4]} points")
            point_total += scoring[-4]

        elif dist_from_center < 5:
            print(f"{colors[-5]}: {scoring[-5]} point")
            point_total += scoring[-5]

        else:
            print("Outside target: no points")

    print(f"Total Points = {point_total}")

    # click to quit
    win.getMouse()
    win.close()


main()
