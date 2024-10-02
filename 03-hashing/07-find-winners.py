# Find Players With Zero or One Losses

# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

#     answer[0] is a list of all players that have not lost any matches.
#     answer[1] is a list of all players that have lost exactly one match.

# The values in the two lists should be returned in increasing order.

# Note:

#     You should only consider the players that have played at least one match.
#     The testcases will be generated such that no two matches will have the same outcome.

# Example 1:
# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

# Example 2:
# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].

 

# Constraints:
#   1 <= matches.length <= 10^5
#   matches[i].length == 2
#   1 <= winneri, loseri <= 10^5
#   winneri != loseri
#   All matches[i] are unique.


from collections import defaultdict
def find_winners(matches: list[list[int]]) -> list[list[int]]:    
    wins = defaultdict(int)
    losses = defaultdict(int)
    result = [set(), set()]
    
    for winner, loser in matches:
        wins[winner] += 1 
        losses[loser] += 1
    
    for winner, loser  in matches:
        if  winner not in losses:
            result[0].add(winner)
            
        if losses[loser] == 1:
            result[1].add(loser)
            
    return [list(sorted(result[0])), list(sorted(result[1]))]


import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
        expected_output = [[1,2,10],[4,5,7,8]]
        self.assertEqual(find_winners(matches), expected_output)
        
    def test_example_2(self):
        matches = [[2,3],[1,3],[5,4],[6,4]]
        expected_output = [[1,2,5,6],[]]
        self.assertEqual(find_winners(matches), expected_output)
    
    
if __name__ == '__main__':
    unittest.main()