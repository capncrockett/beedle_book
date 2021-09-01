# c10ex04.py
#     Extended Three Button Monte
from random import randrange
from graphics import *
from button import Button


def get_door_pick(win, b1, b2, b3):
    # waits for a click in b1, b2, or b3
    # returns the number of the door clicked
    choice = None
    while choice is None:
        pt = win.getMouse()
        for button in [b1, b2, b3]:
            if button.clicked(pt):
                choice = button

    choice_num = int(choice.get_label()[-1])
    return choice_num


def update_score(choice, msg, score, hits, misses):
    # Compares choice to a random number
    # Displays win or loss in msg
    # Updates hits or misses and display of score
    # Returns updated hits and misses
    secret = randrange(1,4)
    tally_str = "Wins: {0:2}   Losses: {1:2}"
    if choice == secret:
        msg.setText("You win!")
        hits = hits + 1
    else:
        msg.setText("You lose. The answer was door {0}.".format(secret))
        misses = misses + 1
    score.setText(tally_str.format(hits,misses))
    return hits, misses


def quit_or_play(win, quit, again):
    # Get a click in quit or again
    # Returns True if again clicked, false for quit
    quit.activate()
    again.activate()
    pt = win.getMouse()
    while not (quit.clicked(pt) or again.clicked(pt)):
        pt = win.getMouse()
    ans = again.clicked(pt)
    quit.deactivate()
    again.deactivate()
    return ans


def main():

    # Set up interface
    win = GraphWin("Extended Three Button Monte", 350, 350)
    win.setCoords(.5,-2, 3.5, 3)
    b1 = Button(win, Point(1,2), .75, 1, "Door 1")
    b1.activate()
    b2 = Button(win, Point(2,2), .75, 1, "Door 2")
    b2.activate()
    b3 = Button(win, Point(3,2), .75, 1, "Door 3")
    b3.activate()
    again = Button(win, Point(1.25,0), 1, .75, "Play Again")
    quit = Button(win, Point(2.75,0), 1, .75, "Quit")
    mess = Text(Point(2,.75), "Guess a door")
    mess.setStyle("bold")
    mess.draw(win)
    score_box = Text(Point(2,-1), "")
    score_box.draw(win)

    play_again = True
    hits = 0
    misses = 0
    while play_again:
        mess.setText("Guess a door")
        pick = get_door_pick(win, b1, b2, b3)
        hits, misses = update_score(pick, mess, score_box, hits, misses)
        play_again = quit_or_play(win, quit, again)
    win.close()


if __name__ == '__main__':
    main()
