# five_click_house.py
# A program that allows the user to draw a house in five clicks.

from graphics import *
from button import Button
from random import randint


def main():
    # draw window and set coords
    win = GraphWin("Five Click House", 600, 600)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("white")
    message = Text(Point(3, 9), "The Five Click House. Click to start.")
    message.draw(win)
    win.getMouse()

    # draw house frame
    message.setText("Click on lower left corner of frame.")
    frame_ll = win.getMouse()
    frame_ll.draw(win)
    message.setText("Click on upper right corner of frame.")
    frame_ur = win.getMouse()
    frame_ur.draw(win)
    frame = Rectangle(frame_ll, frame_ur)
    frame.setFill("green")
    frame.draw(win)

    # draw door
    house_width = frame_ll.getX() - frame_ur.getX()
    door_width = house_width / 5
    half_door = door_width / 2
    message.setText("Click on top center of door frame.")
    p3 = win.getMouse()
    p3.draw(win)
    door_ll_x = p3.getX() - half_door
    door_ur_x = p3.getX() + half_door
    door = Rectangle(Point(door_ll_x, frame_ll.getY()),
                     Point(door_ur_x, p3.getY()))
    door.setFill("red")
    door.draw(win)

    # draw window
    message.setText("Click on center of window.")
    window_center = win.getMouse()
    window_width = door_width / 2
    half_window = window_width / 2
    win_point_1 = window_center.clone()
    win_point_1.move(-half_window, half_window)
    win_point_2 = window_center.clone()
    win_point_2.move(half_window, -half_window)
    window = Rectangle(win_point_1, win_point_2)
    window.setFill("white")
    window.draw(win)

    # draw roof
    message.setText("Click on the peak of the roof.")
    peak = win.getMouse()
    frame_ul = frame_ur.clone()
    frame_ul.move(house_width, 0)
    roof = Polygon(frame_ul, peak, frame_ur)
    roof.setFill("black")
    roof.draw(win)

    quit_button = Button(win, Point(3, 1), 1, 1, "Quit")
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        print(randint(0, 100))
        quit_button.activate()
        pt = win.getMouse()
    win.close()


main()
