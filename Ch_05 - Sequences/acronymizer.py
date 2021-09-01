# acronymizer.py
#   Program makes an acronym out of your phrase.

def main():
    print('Welcome to the "acronymizer".')
    phrase = input('Enter a phrase to "acronymize": ')
    acronym = ""
    for word in phrase.split():
        acronym = acronym + word[0]
    print(f"Your acronym is {acronym.upper()}.")


main()
