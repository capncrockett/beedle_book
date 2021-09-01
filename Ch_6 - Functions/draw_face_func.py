# # draw_face_func.py
# from graphics import *
#
#
# def draw_face(center, size, win):
#     """Draws a face.
#
#     :param center: Graph Point
#     :param size: int
#     :param win: GraphWin
#     :return: A window with a face.
#     """
#     cen_x = center[0]
#     cen_y = center[1]
#
#     # draw main face
#     face = Circle(Point(cen_x, cen_y), size)
#     face.setFill("gray")
#     face.draw(win)
#
#     # draw two eyes
#     eye_1 = Circle(Point((cen_x - (cen_x / 3)), (cen_y + (cen_y / 4))), size/10)
#     eye_2 = Circle(Point((cen_x + (cen_x / 3)), (cen_y + (cen_y / 4))), size/10)
#     eye_1.setFill("black")
#     eye_2.setFill("black")
#     eye_1.draw(win)
#     eye_2.draw(win)
#
#     # # draw nose
#     # nose = Rectangle(Point(center[0] - 0.2, center[1] - 0.2),
#     #                  Point(center[0] + 0.2, center[1] + 0.2),)
#     # nose.setFill("black")
#     # nose.draw(win)
#     #
#     # # draw mouth
#     # upper_teeth = Text(Point(center[0], center[1] - 1), "VVVVVVVVV")
#     # upper_teeth.setSize(12)
#     # upper_teeth.setStyle("bold")
#     # upper_teeth.draw(win)
#     # lower_teeth = Text(Point(center[0], center[1] - 1.5), "^^^^^^^")
#     # lower_teeth.setSize(16)
#     # lower_teeth.setStyle("bold")
#     # lower_teeth.draw(win)
#
#     # click to quit
#     win.getMouse()
#     win.close()
#
#
# def test():
#     win = GraphWin("Face", 400, 400)
#     win.setCoords(0.0, 0.0, 10, 10)
#
#     # draw_face((Center Point(x,y), size(int), ???)
#     draw_face((3, 5), 3, win)
#
#
# test()

# # c06ex15.py
# #   face drawing program
#
#
# from graphics import *
#
#
# def draw_face(center, size, window):
#     eye_size = 0.15 * size
#     eye_off = size / 3.0
#     mouth_size = 0.8 * size
#     mouth_off = size / 2.0
#     head = Circle(center, size)
#     head.setFill("yellow")
#     head.draw(window)
#     left_eye = Circle(center, eye_size)
#     left_eye.move(-eye_off, -eye_off)
#     right_eye = Circle(center, eye_size)
#     right_eye.move(eye_off, -eye_off)
#     left_eye.draw(window)
#     right_eye.draw(window)
#     p1 = center.clone()
#     p1.move(-mouth_size/2, mouth_off)
#     p2 = center.clone()
#     p2.move(mouth_size/2, mouth_off)
#     mouth = Line(p1, p2)
#     mouth.draw(window)
#
#
# def test():
#     win = GraphWin("Faces")
#     draw_face(Point(50, 50), 10, win)
#     draw_face(Point(100, 100), 20, win)
#     draw_face(Point(150, 150), 30, win)
#     win.getMouse()
#     win.close()
#
#
# test()
