# Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> from graphics import *
# >>> win = GraphWin()
# >>> win.close()
# >>> win = GraphWin()
# >>> *
# SyntaxError: invalid syntax
# >>> from graphics import *
# >>> win = GraphWin()
# >>> win.close()
# >>> win.close()
# >>> win.close()
# >>> win = GraphWin()
# >>> p = Point(50, 60)
# >>> p.getX()
# 50.0
# >>> p.getY()
# 60.0
# >>> win = GraphWin()
# >>> p.draw(win)
# Point(50.0, 60.0)
# >>> p2 = Point(140, 100)
# >>> p2.draw(win)
# Point(140.0, 100.0)
# >>> #### oOpen a graphics window
# >>> win = Graphwin('Shapes')
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     win = Graphwin('Shapes')
# NameError: name 'Graphwin' is not defined
# >>> *
# SyntaxError: invalid syntax
# >>> import *
# SyntaxError: invalid syntax
# >>>
# >>> from graphics import *
# >>> win = GraphWin('Shapes')
# >>> center = Point(100, 100)
# >>> circ = Circle(center, 30)
# >>> circ.setFill('red')
# >>> circ.draw(win)
# Circle(Point(100.0, 100.0), 30)
# >>> label = Text(center, "Red Circle")
# >>> label.draw(win)
# Text(Point(100.0, 100.0), 'Red Circle')
# >>> rect = Rectangle(Point(30,30), Point(70,70))
# >>> rect.draw(win)
# Rectangle(Point(30.0, 30.0), Point(70.0, 70.0))
# >>> line = Line(Point(20,30), Point(180,165))
# >>> line.draw(win)
# Line(Point(20.0, 30.0), Point(180.0, 165.0))
# >>> oval = Oval(Point(20,30), Point(180,199))
# >>> oval.draw(win)
# Oval(Point(20.0, 30.0), Point(180.0, 199.0))
# >>> oval = Oval(Point(20,150), Point(180,199))
# >>> oval.draw(win)
# Oval(Point(20.0, 150.0), Point(180.0, 199.0))
# >>>