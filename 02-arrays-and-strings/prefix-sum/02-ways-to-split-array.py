# Number of Ways to Split Array

# Given an 
#   integer array nums, 
# find 
#   the number of ways to split the array 
# into 
#   two parts 
# so that 
#   the first section 
#       has a sum greater than or equal to 
#       the sum of the second section. 
#   The second section 
#       should have at least one number.

def ways_to_split_array(nums: list[int]) -> int:
    prefix = [nums[0]]
    
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
        
    ans = 0
    
    for i in range(len(nums) -1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans += 1
            
    return ans


def ways_to_split_array_improoved(nums: list[int]) -> int:
    left_section = ans = 0
    total = sum(nums)
    
    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1
    return ans

print(ways_to_split_array_improoved([10,4,-8,7]))