# happy.py

def happy():
    return "Happy birthday to you!\n"


def verse_for(person):
    lyrics = happy() * 2 + "Happy birthday, dear " + person + ".\n" + happy()
    return lyrics


def main():
    outf = open("Happy_Birthday.txt", "w")
    for person in ["Fred", "Lucy", "Elmer"]:
        print(verse_for(person), file=outf)
    outf.close()


main()
