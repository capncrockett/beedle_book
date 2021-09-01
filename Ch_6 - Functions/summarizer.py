# summarizer.py

def sum_list(nums):
    total = 0
    for i in nums:
        total = total + i
    return total


def test():
    nums = list(range(10))
    print(sum_list(nums))


test()
