# square_this.py

def square_this(nums: list) -> list:
    """Squares numbers in a list. Returns a new list."""
    new_list = []
    for i in nums:
        new_list.append(i ** 2)
    return new_list


def main():
    list_1 = [1, 2, 3]
    list_2 = [3, 4, 5]
    new_list_1 = square_this(list_1)
    new_list_2 = square_this(list_2)
    print(list_1, new_list_1)
    print(list_2, new_list_2)


main()


# c06ex11.py
#    Square each value in a list

def square_each(nums):
    """Squares numbers from a list in place. Returns modified list."""
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def test():
    nums = list(range(10))
    square_each(nums)
    print(nums)


test()
