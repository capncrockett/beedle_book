# regression_line.py
#   Plots a line of regression based on mouse click input from the user.
#   Would be good to rewrite so it uses a list instead.
from graphics import *

# These two "constants" are defined here so they can be used in multiple
#    functions to draw the done button and check to see if it is clicked in.

done_x = 1.0
done_y = 0.75


def create_window():
    # Creates a 600x600 window titled "Linear Regression" and draws a
    #   "Done" button in the lower left corner. Coords are 0, 0 to
    #   10, 10. Upper right corner of the done button is located at
    #   done_x, done_y.
    # Returns the window
    win = GraphWin("Linear Regression", 600, 600)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("gray")

    # draw done button to finish in the lower left
    done_button = Rectangle(Point(.05, 0), Point(done_x, done_y))
    done_button.draw(win)
    Text(done_button.getCenter(), "Done").draw(win)
    return win


def get_point(w):
    # w is a GraphWin
    # Pauses for user to click in window(w). If user clicks somewhere
    #   other than the Done button, the point is drawn in w.
    # Returns the point(p) clicked, or None if user clicked the Done.
    p = w.getMouse()
    if p.getX() > done_x or p.getY() > done_y:
        p.draw(w)
        return p
    else:
        return None


def slope(xb, yb, xx, xy, n):
    # Returns the slope of the line of best fit, also known as m.
    return (xy - n * xb * yb) / (xx - n * xb * xb)


def predict(x, xb, yb, m):
    # Returns a predicated value for y.
    return yb + m * (x - xb)


def get_points(w):
    # Allows the user to make a series of mouse clicks in window(w)
    #   until the user clicks in the Done button.
    # Returns: average of x values
    #          average of y values
    #          sum of the squares of the x values
    #          sum of the xy products
    #          the number of points clicked before Done
    sum_x = 0.0
    sum_y = 0.0
    sum_x_sq = 0.0
    sum_xy = 0.0
    n = 0
    p = get_point(w)
    while p is not None:
        x, y = p.getX(), p.getY()
        sum_x = sum_x + x
        sum_y = sum_y + y
        sum_x_sq = sum_x_sq + x * x
        sum_xy = sum_xy + x * y
        n = n + 1
        p = get_point(w)
    return sum_x / n, sum_y / n, sum_x_sq, sum_xy, n


def main():
    # Draws a window, gets mouse clicks and then draws line of best
    #   fit through the points that were clicked.
    win = create_window()
    xbar, ybar, sum_x_sq, sum_xy, n = get_points(win)
    m = slope(xbar, ybar, sum_x_sq, sum_xy, n)
    y1 = predict(0, xbar, ybar, m)
    y2 = predict(10, xbar, ybar, m)
    reg_line = Line(Point(0, y1), Point(10, y2))
    reg_line.setWidth(2)
    reg_line.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
