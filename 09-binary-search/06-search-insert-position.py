# Search Insert Position

# Given a sorted array of 
#   distinct integers and 
#   a target value, 

# return 
#   the index if the target is found. 
# If not, 
# return 
#   the index where it would be if it were inserted in order.

# Example 
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Constraints
#  1 <= nums.length <= 104
#  -104 <= nums[i] <= 104
#  nums contains distinct values sorted in ascending order.
#  -104 <= target <= 104

def search_insert_position(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        num = nums[mid]
        if num == target:
            return mid
        elif num > target:
            right = right -1
        else:
            left = left + 1
    
    return left

print(search_insert_position([1,3,5,6], 5))
