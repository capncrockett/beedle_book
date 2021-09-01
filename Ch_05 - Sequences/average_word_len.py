# average_word_len
#   Find the average word length of a sentence.

def main():
    print("This program finds the average word length of a sentence.")
    print()

    sentence = input("Type a sentence: ")

    word_count = sentence.count(' ') + 1
    words = sentence.split()
    letter_count = 0

    for letters in words:
        letter_count = letter_count + len(letters)

    avg_word_length = letter_count // word_count

    print(f"Letter count: {letter_count} ")
    print(f"Word count: {word_count}")
    print(f"Average word length: {avg_word_length}")


main()

# # c05ex10.py
# #   Average word length
#
#
# def main():
#     print("Average word length")
#     print()
#
#     phrase = input("Enter a phrase: ")
#
#     # using accumulator loop
#     count = 0
#     total = 0
#     for word in phrase.split():
#         total = total + len(word)
#         count = count + 1
#
#     print("Average word length", total / count)
#
#
# main()
