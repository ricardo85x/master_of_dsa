# Minimum Operations to Halve Array Sum

# You are given an array nums of positive integers. 
# In one operation, you can choose any number 
# from nums and reduce it to exactly half the number. 

# Return the minimum number of operations 
# to reduce the sum of nums by at least half.


import heapq

def halve_array(nums: list[int]) -> int: 
    target = sum(nums) / 2
    heap = [-item for item in nums]
    ans = 0
    
    while target > 0:
        ans += 1
        x = heapq.heappop(heap)
        target += x / 2
        heapq.heappush(heap, x / 2)
        
    return  ans


import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        nums = [5,19,8,1]
        expected_output = 3
        self.assertEqual(halve_array(nums), expected_output)
        
if __name__ == '__main__':
    unittest.main()