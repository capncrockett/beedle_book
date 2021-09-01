# face_scrubber.py
from graphics import *
import math

def draw_face(center, size, win):
    eye_size = 0.15 * size
    eye_off = size / 3.0
    mouth_size = 0.8 * size
    mouth_off = size / 2.0
    head = Circle(center, size)
    head.setFill("yellow")
    head.draw(win)
    left_eye = Circle(center, eye_size)
    left_eye.move(-eye_off, -eye_off)
    right_eye = Circle(center, eye_size)
    right_eye.move(eye_off, -eye_off)
    left_eye.draw(win)
    right_eye.draw(win)
    p1 = center.clone()
    p1.move(-mouth_size/2, mouth_off)
    p2 = center.clone()
    p2.move(mouth_size/2, mouth_off)
    mouth = Line(p1, p2)
    mouth.draw(win)


def main():
    print("Program to put smiley faces on an image.")
    # fname = input("Enter filename: ")
    fname = "joe and steven at bach fest.gif"

    my_image = Image(Point(960/2, 836/2), fname)
    width = my_image.getWidth()
    height = my_image.getHeight()

    win = GraphWin("Face", width, height)
    my_image.draw(win)

    # ask for number of faces to block
    faces = int(input("How many faces do you need to block?: "))

    # for loop for the number of faces
    for point in range(faces):
        print("Click the center of a face...")
        center = win.getMouse()
        print("Click the edge of that face...")
        edge = win.getMouse()
        p1 = edge.getX() - center.getX()
        p2 = edge.getY() - center.getY()
        size = math.sqrt(p1 ** 2 + p2 ** 2)
        draw_face(center, size, win)
        print()

    print("Click anywhere to QUIT")
    win.getMouse()
    win.close()


main()
