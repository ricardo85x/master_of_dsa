# Given an integer array nums, 
# find all the unique numbers x in nums 
# that satisfy the following: 
# x + 1 is not in nums, 
# and x - 1 is not in nums.


def find_mumbers(nums: list[int]) -> list[int]:
    result = []
    uniques = set(nums)

    for i in uniques:
        if i + 1 not in uniques and i - 1 not in uniques:
            result.add(i)
    
    return result

