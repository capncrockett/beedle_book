# futval_graph.py

from graphics import *


def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    # principal = float(input("Enter the initial principal: "))
    # apr = float(input("Enter the annualized interest rate: "))
    principal = 2000
    apr = 0.1

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setCoords(-1.75, -200, 11.5, 10400)
    win.setBackground("white")
    Text(Point(-1, 0), ' 0.0k').draw(win)
    Text(Point(-1, 2500), ' 2.5k').draw(win)
    Text(Point(-1, 5000), ' 5.0k').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0k').draw(win)

    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()


main()
