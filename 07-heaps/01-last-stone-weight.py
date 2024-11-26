# Last Stone Weight

# You are given an array of integers stones 
#   where stones[i] is the weight of the ithith stone. 
# On each turn, we choose the heaviest two stones 
#   and smash them together. 
# Suppose the heaviest two stones 
#   have weights x and y with x <= y. 
# If x == y, 
#   then both stones are destroyed. 
# If x != y, 
#   then x is destroyed and y loses x weight. 
# Return the weight of the last remaining stone, 
#   or 0 if there are no stones left.

import heapq

def last_stone_weight(stones: list[int]) -> int:
    
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = abs(heapq.heappop(stones))
        second = abs(heapq.heappop(stones))
        
        if first != second:
            heapq.heappush(stones, -abs(first - second))

    return -stones[0] if stones else 0


# Python's heap implementation only implements min heaps. 
# To simulate a max heap, we can just make all values we put on the heap negative.

import unittest
class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        stones = [2,7,4,1,8,1]
        expected_output = 1
        self.assertEqual(last_stone_weight(stones), expected_output)
        
    
    def test_example_2(self):
        stones = [6,4,8,12,10,22]
        expected_output = 2
        self.assertEqual(last_stone_weight(stones), expected_output)

if __name__ == '__main__':
    unittest.main()