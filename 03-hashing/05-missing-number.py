# Given an array nums containing n distinct numbers 
# in the range [0, n], 
# return the only number in the range 
# that is missing from the array.

def missing_numbers(nums: list[int]) -> list[int]:
    result = []
    num_set = set(nums)

    if 0 not in num_set:
        return 0

    last_index = 0

    for i in range(len(num_set)):
        if i not in num_set:
            return i

    return num_set[last_index] + 1