# acronymizer_func.py
#   Program makes an acronym out of your phrase.

def acronymizer(phrase):
    acronym = ""
    for word in phrase.split():
        acronym = acronym + word[0]
    return acronym.upper()


def main():
    print('Welcome to the "acronymizer".\n')
    phrase = input('Enter a phrase to "acronymize": ')
    print(f"Your acronym is {acronymizer(phrase)}.")


main()
