# c04ex11.pyw
#   build a house with 5 mouse clicks

from graphics import *


def main():
    win = GraphWin("Design a House", 500, 500)
    win.setCoords(0, 0, 200, 200)
    message = Text(Point(100, 5), "")
    message.draw(win)

    # Draw the frame of the house
    message.setText("Click on lower left corner of the frame")
    frame_ll = win.getMouse()
    frame_ll.draw(win)
    message.setText("Click upper right corner of the frame")
    frame_ur = win.getMouse()
    frame_ll.undraw()
    Rectangle(frame_ll, frame_ur).draw(win)

    # Draw a door
    house_width = frame_ur.getX() - frame_ll.getX()
    door_width = 0.2 * house_width
    half_door = door_width/2.0
    message.setText("Click on the center of the top of the door")
    door_pt2 = win.getMouse()
    door_pt2.move(half_door, 0)
    door_x1 = door_pt2.getX() - door_width
    door_y1 = frame_ll.getY()
    door = Rectangle(Point(door_x1, door_y1), door_pt2)
    door.setFill("red")
    door.draw(win)

    # Draw a window
    message.setText("Click on the center of the window")
    window_center = win.getMouse()
    w1 = window_center.clone()
    win_off = 0.5 * half_door
    w1.move(-win_off, win_off)
    w2 = window_center.clone()
    w2.move(win_off, -win_off)
    Rectangle(w1, w2).draw(win)

    # Draw the roof
    message.setText("Click on the peak of the roof")
    peak = win.getMouse()
    frame_ul = frame_ur.clone()
    frame_ul.move(-house_width, 0)
    roof = Polygon(frame_ul, peak, frame_ur)
    roof.draw(win)
    roof.setFill("black")

    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()
