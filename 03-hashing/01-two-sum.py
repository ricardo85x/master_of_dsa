# Given an array of integers nums and an integer target, 
# return indices of two numbers 
# such that they add up to target. 
# You cannot use the same index twice.

def twoSum(nums: list[int], target: int) -> list[int]:
    dic = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:
            return [i, dic[complement]]
        dic[num] = i
    
    return [-1, -1]

print(twoSum([5,2,7,10,3,9], 17))
