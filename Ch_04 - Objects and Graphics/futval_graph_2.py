# futval_graph.py

from graphics import *


def main():
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(5, 9600),   "Principal:").draw(win)
    Text(Point(5.1, 8700), "      APR:").draw(win)

    # draw measurements
    win.setBackground("white")
    Text(Point(-1, 0), ' 0.0k').draw(win)
    Text(Point(-1, 2500), ' 2.5k').draw(win)
    Text(Point(-1, 5000), ' 5.0k').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0k').draw(win)

    # get input
    principal = Entry(Point(7, 9600), 10)
    principal.setText("0.0")
    principal.draw(win)
    apr = Entry(Point(6.5, 8700), 5)
    apr.setText("0.0")
    apr.draw(win)

    # wait for a mouse click
    button = Text(Point(6, 7500), "Click to calculate")
    button.draw(win)
    Rectangle(Point(4.5, 7000), Point(7.5, 8000)).draw(win)
    win.getMouse()

    # convert input
    principal = float(principal.getText())
    apr = float(apr.getText())

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
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    # click to quit
    button.setText("Quit")
    win.getMouse()
    win.close()


main()
