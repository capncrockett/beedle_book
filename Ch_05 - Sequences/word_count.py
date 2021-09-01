# word_count.py
#   A program for counting the words in a sentence.

def main():
    print("This is a word counter.")
    print()

    sentence = input("Please type your sentence here: ")

    # using an accumulator
    word_count = 0
    for i in sentence.split():
        word_count = word_count + 1

    # alternatives:
    # word_count = len(sentence.split())
    # word_count = sentence.count(' ') + 1

    print(f"Your sentence contains {word_count} words.")


main()
