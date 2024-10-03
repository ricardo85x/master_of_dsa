# Maximum Number of Balloons

# Given a string text, 
# you want to use the characters of text 
# to form as many instances 
# of the word "balloon" as possible.

# You can use each 
# character in text at most once. 
# Return the maximum number 
# of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "ricardo"
# Output: 0

# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import defaultdict
def max_number_of_balloons(text: str) -> int:
    target_word = "balloon"
    hash_ballon = defaultdict(int)
    for c in target_word:
        hash_ballon[c] += 1
    
    hash_target = defaultdict(int)
    for c in text:
        hash_target[c] += 1
        
    combinations = set()
    for k, v in hash_ballon.items():
        target_count = hash_target[k]
        if target_count == 0:
            return 0
        
        combinations.add(target_count // v)
        
    return min(combinations)

from collections import Counter
def max_number_of_balloons_with_counter(text: str) -> int:
    balloon_counter = Counter('balloon')
    target_counter = Counter(text)
    
    combinations = set()
    
    for k, v in balloon_counter.items():
        if target_counter[k] == 0:
            return 0
        combinations.add(target_counter[k] // v)
        
    return min(combinations)
    
    
    
   



import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        text = "nlaebolko"
        expected_output = 1
        self.assertEqual(max_number_of_balloons_with_counter(text), expected_output)
        
    def test_example_2(self):
        text = "loonbalxballpoon"
        expected_output = 2
        self.assertEqual(max_number_of_balloons_with_counter(text), expected_output)
        
    def test_example_3(self):
        text = "ricardo"
        expected_output = 0
        self.assertEqual(max_number_of_balloons_with_counter(text), expected_output)
        
if __name__ == "__main__":
    unittest.main()