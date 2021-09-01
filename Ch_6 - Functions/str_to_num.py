# # str_to_num.py
# #   Function to convert strings to ints.
#
# def to_numbers(str_list):
#     """Converts string numbers to int. Returns new list."""
#     int_list = []
#     for i in str_list:
#         int_list.append(int(i))
#     return int_list
#
#
# def test():
#     string_list_1 = ['1', '2', '3']
#     print(to_numbers(string_list_1))
#
#
# test()
#

# string_list = ["1", "2", "3"]
# int_list = []
# for i in string_list:
#     int_list.append(int(i))
#
# for obj in int_list:
#     print(type(obj))


def mod_to_num(str_list):
    """Returns string numbers to float. Modified list."""
    for i in range(len(str_list)):
        str_list[i] = float(str_list[i])


def test():
    string_list_1 = ['1', '2', '3.14', '42']
    mod_to_num(string_list_1)
    print(string_list_1)


test()

