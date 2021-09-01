# post_test_loop.py

# *** Two examples ***

number = -1     # Start with an illegal value to get into the loop.
while number < 0:
    number = float(input("Enter a positive number: "))
    if number < 0:
        print("The number you entered was not positive.")

while True:
    number = float(input("Enter a positive number: "))
    if number >= 0:
        break   # Exit loop if number is valid.
    else:
        print("The number you entered was not positive.")
