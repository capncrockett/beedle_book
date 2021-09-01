# event_loop_2.py --- color-changing window
from graphics import *


def handle_key(k, win):
    # process the key
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")


def handle_click(pt, win):
    # create an Entry for user to type in
    entry = Entry(pt, 10)
    entry.draw(win)

    # Go modal: loop until user types <Enter> key
    # Obvious...
    while True:
        key = win.getKey()
        if key == "Return":
            break

    # # Clever... Stick with obvious (i.e. Explicit)
    # while win.getKey() != "Return":
    #     pass

    # un-draw the entry and create and draw Text()
    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)

    # clear (ignore) any mouse click that occurred during text entry
    win.checkMouse()


def main():
    win = GraphWin("Color Window", 500, 500)

    # Event Loop: handle key presses and mouse clicks until the user
    #   presses the "q" key.
    while True:
        key = win.checkKey()
        if key == "q" or key == "Escape":  # loop exit
            break

        if key:
            handle_key(key, win)

        pt = win.checkMouse()
        if pt:
            handle_click(pt, win)

    # exit program
    win.close()


main()
