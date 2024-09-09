# Binary Search
# You are given an array of integers nums 
# which is sorted in ascending order, 
# and an integer target. 
# If target exists in nums, 
# return its index. 
# Otherwise, return -1.


def find_index(nums: list[int], target: int) -> int:
    left = 0
    right =  len(nums) - 1
        
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

print(find_index([1,4,8,13,20], 4))
