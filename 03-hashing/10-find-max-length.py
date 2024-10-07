# Contiguous Array

# Given a binary array nums, 
# return the maximum length 
# of a contiguous subarray 
# with an equal number of 0 and 1.

# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: 
#   [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:
# Input: nums = [0,1,0]
# Output: 2
# Explanation: 
#   [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.

from collections import Counter
def find_max_length(nums: list[int]) -> int:
    hash_map = { 0: -1}
    max_len = count = 0
    
    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1
        if count in hash_map:
            max_len = max(max_len, i - hash_map[count])
        else:
            hash_map[count] = i
    return max_len
        
        
import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        nums = [0,1]
        expected_output = 2
        self.assertEqual(find_max_length(nums), expected_output)
        
    def test_example_2(self):
        nums = [0,1,0]
        expected_output = 2
        self.assertEqual(find_max_length(nums), expected_output)  
        
    def test_example_3(self):
        nums = [0, 1, 1, 0]
        expected_output = 4
        self.assertEqual(find_max_length(nums), expected_output)  
    

if __name__ == "__main__":
    unittest.main()