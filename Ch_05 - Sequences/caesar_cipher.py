# caesar cipher.py
#   A program for encoding a message using a caesar cipher.

def main():
    print("This program uses a Caesar cipher to encode your message.")
    message = input("Please enter message for encoding: ")
    key = int(input("Enter the key value: "))
    encoded_msg = ""
    for char in message:
        # char_ord = ord(char)
        # char_ord_key = char_ord + key
        # char_chr_key = chr(char_ord_key)
        encoded_char = chr(ord(char) + key)
        encoded_msg = encoded_msg + encoded_char
    print(f"Encoding complete: {encoded_msg}")


main()

# # c05ex07.py
# #    Caesar cipher (non-circular)
#
#
# def main():
#     print("Caesar cipher")
#     print()
#
#     key = int(input("Enter the key value: "))
#     plain = input("Enter the phrase to encode: ")
#     cipher = ""
#     for letter in plain:
#         cipher = cipher + chr(ord(letter) + key)
#
#     print("Encoded message follows:")
#     print(cipher)
#
#
# main()
