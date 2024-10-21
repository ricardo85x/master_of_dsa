# Subsets

# Given an integer array nums of unique elements, 
# return all subsets in any order without duplicates.

# For example, 
# given 
#   nums = [1, 2, 3], 
# return [
#   [],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]
# ]

def subsets(nums: list[int]) -> list[list[int]]:
    def backtrack(curr, i):
        if i > len(nums):
            return
        ans.append(curr[:])
        for j in range(i, len(nums)):
            curr.append(nums[j])
            backtrack(curr, j + 1)
            curr.pop()
    
    ans = []
    backtrack([], 0)
    return ans

print(subsets([10,50,100]))


import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        nums = [1,2,3]
        expected_output = [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
        self.assertEqual(subsets(nums), expected_output)
        
    def test_example_2(self):
        nums = [1,10,100]
        expected_output = [[], [1], [1,10], [1,10, 100], [1,100], [10], [10,100], [100]]
        self.assertEqual(subsets(nums), expected_output)
        
if __name__ == "__main__":
    unittest.main()