# average_2.py

# initialize total to 0.0
# initialize count to 0
# set more_data to 'yes'
# while more_data is 'yes'
    # get the next data item
    # input a number, x
    # process the item
    # add x to total
    # add 1 to count
    #ask user if there is more_data
# output total / count

total = 0.0
count = 0
more_data = 'yes'
while more_data[0] == 'y':
    x = eval(input("Enter a number >> "))
    total = total + x
    count = count + 1
    more_data = input("Do you have more numbers (yes or no)? ")
print(f"The average number is {total / count}")

