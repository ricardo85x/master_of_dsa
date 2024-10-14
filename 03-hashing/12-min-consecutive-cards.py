# Minimum Consecutive Cards to Pick Up

# Given an integer array cards, 
# find the length of the shortest subarray 
# that contains at least one duplicate. 
# If the array has no duplicates, 
# return -1.

# Example 1
# Input:
#   cards = [1, 2, 6, 2, 1]
# Output:
# 3

# Example 2
# Input:
#   cards = [3, 4, 2, 3, 4, 7]
# Output:
# 4

from collections import defaultdict
def minimum_card_pickup(cards: list[int]):
    dic = defaultdict(list)
    for i in range(len(cards)):
        dic[cards[i]].append(i)
        
    ans = float('inf')
    for key in dic:
        arr = dic[key]
        for i in range(len(arr) - 1):
            ans = min(ans, arr[i + 1] - arr[0] + 1)
    
    return ans if ans < float('inf') else -1

def minimum_card_pickup_v2(cards: list[int]) -> int:
    dic = defaultdict(list)
    ans = float('inf')
    for i in range(len(cards)):
        if cards[i] in dic:
            ans = min(ans, i - dic[cards[i]] + 1)
        
        dic[cards[i]] = i
        
    return ans if ans < float('inf') else -1
    
    

import unittest
class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        cards = [1, 2, 6, 2, 1]
        expected_output = 3
        self.assertEqual(minimum_card_pickup(cards), expected_output)
        
    def test_example_2(self):
        cards = [3, 4, 2, 3, 4, 7]
        expected_output = 4
        self.assertEqual(minimum_card_pickup(cards), expected_output)    

if __name__ == "__main__":
    unittest.main()