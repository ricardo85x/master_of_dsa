# Squares of a Sorted Array

# Given an integer array nums 
# sorted in non-decreasing order, 
# return an array of the squares of each number 
# sorted in non-decreasing order.

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def sortedSquares(nums: list[int]) -> list[int]:
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1
    
    for i in range(len(nums) - 1, -1, -1):
        square = 0
        if(abs(nums[left]) < abs(nums[right])):
            square = nums[right] ** 2
            right -= 1
        else:
            square = nums[left] ** 2
            left += 1
        result[i] = square
    
    return result 

print(sortedSquares([-4,-1,0,3,10]))
