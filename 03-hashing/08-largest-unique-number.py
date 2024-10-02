# Largest Unique Number

# Given an integer array nums, 
# return the largest integer that only occurs once. 
# If no integer occurs once, return -1.


# Example 1:
# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: 
# The maximum integer in the array is 9 but it is repeated. 
# The number 8 occurs only once, so it is the answer.

# Example 2:
# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.

 

# Constraints:
# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 1000

from collections import defaultdict

def largest_unique_number(nums: list[int]) -> int:
    
    uniques = defaultdict(int)
    
    for n in nums:
        uniques[n] += 1
        
    result = -1
    for key, val in uniques.items():
        if val == 1 and key > result:
            result = key
    
    return result

import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        nums = [5,7,3,9,4,9,8,3,1]
        expected_result = 8
        self.assertEqual(largest_unique_number(nums), expected_result)
        
    def test_example_2(self):
        nums = [9,9,8,8]
        expected_result = -1
        self.assertEqual(largest_unique_number(nums), expected_result)
        

if __name__ == "__main__":
    unittest.main()