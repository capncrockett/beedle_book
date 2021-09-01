# happy.py

def happy():
    print("Happy birthday to you!")


def sing(person):
    happy()
    happy()
    print(f"Happy birthday, dear {person}.")
    happy()


def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")
    print()


main()
