# ant_go_marching.py

def ants_go(count):
    return f"The ants go marching {count} by {count},"


def hurrah():
    return "hurrah! " * 2


def refrain(count):
    print(ants_go(count), hurrah())
    print(ants_go(count), hurrah())
    print(ants_go(count))


def little_one(action):
    print(f"The little one {action},")


def marching_down():
    print("And they all go marching down...\n"
          "In the ground...\n"
          "To get out...\n"
          "Of the rain.")


def boom():
    print("Boom! " * 3)


def verse(count, action):
    refrain(count)
    little_one(action)
    marching_down()
    boom()


def main():
    variations = [("one", "stopped to suck his thumb"),
                  ("two", "stopped to tie her shoe"),
                  ("three", "stopped to slap his knee"),
                  ("four", "stopped cause she was bored"),
                  ("five", "stopped to feel alive"),
                  ("six", "stopped to play some Styx"),
                  ("seven", "died and went to heaven"),
                  ("eight", "stopped to check his weight"),
                  ("nine", "stopped to drink some wine"),
                  ("ten", "stopped to fuck with Glen")]
    for count, action in variations:
        verse(count, action)
        print()


main()
