# caesar_cipher_round.py
#   A program for encoding a message using a caesar cipher around alphabet.

def main():
    print("This program uses a Caesar cipher to encode your message.")
    print()

    message = input("Enter message for encoding: ")
    key = int(input("Enter the key value: "))
    encoded_msg = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " \
              "abcdefghijklmnopqrstuvwxyz"

    for char in message:
        position = letters.find(char)
        new_position = (position + key) % len(letters)
        encoded_msg = encoded_msg + letters[new_position]

    print("Encoded message as follows:")
    print(encoded_msg)


main()
