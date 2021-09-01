# futval_graph_4.py
from graphics import *


def create_labeled_window():
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0k').draw(win)
    Text(Point(-1, 2500), ' 2.5k').draw(win)
    Text(Point(-1, 5000), ' 5.0k').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0k').draw(win)
    return win


def draw_bar(win, year, height):
    # Draw a bar in window for given year with given height.
    bar = Rectangle(Point(year, 0), Point(year + 1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)


def main():
    print("This program plots the growth of a 10-year investment.")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    win = create_labeled_window()
    draw_bar(win, 0, principal)
    for year in range(1, 11):
        principal = principal * (1 + apr)
        draw_bar(win, year, principal)

    input("Press <Enter> to quit.")
    win.close()


main()
