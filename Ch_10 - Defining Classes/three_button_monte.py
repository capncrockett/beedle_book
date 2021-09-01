# three_button_monte.py
# A graphical representation of three button monte.
from graphics import *
from button import Button
from random import randrange


def get_door_pick(w, d1, d2, d3):
    # randomly pick one of the doors
    winning_door = randrange(1, 4)

    # wait for user to click a door and check if pick was correct
    choice = None
    while choice is None:
        for door in [door_1, door_2, door_3]:
            if door.clicked(pt):
                choice = door

            choice_num = int(choice.get_label()[-1])
            if choice_num == winning_door:
                instructions.setText("Winner!")
            else:
                instructions.setText(f"You lose. The correct door was "
                                     f"{winning_door}. Click anywhere "
                                     f"to try again.")
            print("waiting user input")
            win.getMouse()


def main():
    # Set up all the things...

    # create animation window
    win = GraphWin("Three Door Monte", 350, 350)
    win.setCoords(0, 0, 100, 100)

    # draw a game title and some instructions
    instructions = Text(Point(50, 90), "Choose a door")
    instructions.setStyle('bold')
    instructions.draw(win)
    score_box = Text(Point(50, 25), '')
    score_box.draw(win)

    # draw three buttons(doors) and activate
    door_1 = Button(win, Point(25, 70), 20, 10, 'Door 1')
    door_1.activate()
    door_2 = Button(win, Point(50, 70), 20, 10, 'Door 2')
    door_2.activate()
    door_3 = Button(win, Point(75, 70), 20, 10, 'Door 3')
    door_3.activate()

    # draw quit and try again buttons
    quit_button = Button(win, Point(70, 20), 25, 10, 'Quit')
    try_again = Button(win, Point(30, 20), 25, 10, 'Play Again')

    play_again = True
    hits = 0
    misses = 0
    while play_again:
        instructions.setText("Choose a door")
        choice = get_door_pick(win, door_1, door_2, door_3)
        hits, misses = update_score(pick, instructions, score_box, again)
        play_again = quit_or_play(win, quit, again)
    win.close()



if __name__ == '__main__':
    main()
