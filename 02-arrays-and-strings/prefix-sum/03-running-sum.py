# Running Sum of 1d Array
  
# Given an 
#   array nums. 
# We define 
#   a running sum of an array as 
#       runningSum[i] = sum(nums[0]â€¦nums[i]).
  
# Return the running sum of nums.
  
   
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: 
#   Running sum is obtained as follows: 
#       [1, 1+2, 1+2+3, 1+2+3+4].
  
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: 
#   Running sum is obtained as follows: 
#       [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
  
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
  
# Constraints:
#  1 <= nums.length <= 1000
#  -10^6 <= nums[i] <= 10^6
  
def running_sum(nums: list[int]) -> list[int]:
    result = [nums[0]]
    for i in range(1, len(nums)):
        result.append(nums[i] + result[-1])
    
    return result

import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected_output = [1, 3, 6, 10]
        self.assertEqual(running_sum(nums), expected_output)

    def test_example_2(self):
        nums = [1, 1, 1, 1, 1]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(running_sum(nums), expected_output)

    def test_example_3(self):
        nums = [3, 1, 2, 10, 1]
        expected_output = [3, 4, 6, 16, 17]
        self.assertEqual(running_sum(nums), expected_output)


if __name__ == "__main__":
    unittest.main()