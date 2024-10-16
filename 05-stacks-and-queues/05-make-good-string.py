# Make The String Great

# Given a string s 
# of lower and upper case English letters.

# A good string is a string which 
# doesn't have two adjacent characters s[i] and s[i + 1] where:

#   0 <= i <= s.length - 2
#   s[i] is a lower-case letter and 
#   s[i + 1] is the same letter but in upper-case or vice-versa.

# To make the string good, 
# you can choose two adjacent characters 
# that make the string bad and remove them. 
# You can keep doing this until the string becomes good.

# Return the string after making it good. 
# The answer is guaranteed to be unique 
# under the given constraints.

# Notice that an empty string is also good.


# Example 1:
# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose 
# i = 1 or i = 2, 
# both will result "leEeetcode" to be reduced to "leetcode".

# Example 2:
# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, 
# and all lead to the same answer. 
# For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""

# Example 3:

# Input: s = "s"
# Output: "s"

 
# Constraints:
# 1 <= s.length <= 100
# s contains only lower and upper case English letters.

def make_good_string(s: str) -> str: 
    def sounds_good(s1: str, s2: str) -> bool:
        return abs(ord(s1) - ord(s2)) != 32
    
    def process() -> bool:
        nonlocal s
        
        prev_size = len(s)
        if prev_size <= 1:
            return False
        
        for i in range(len(s) -1):
            if not sounds_good(s[i], s[i + 1]):
                s = s[:i] + s[i+2:]
                break
            
        return len(s) != prev_size
        
    while process():
        continue
         
    return s
    

def make_good_string_v2(s: str) -> str:
    stack = []
    
    for c in s:
        if stack and abs(ord(c) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(c)
              
    return "".join(stack)

import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        s = "leEeetcode"
        expected_output = "leetcode"
        self.assertEqual(make_good_string_v2(s), expected_output)
    
    def test_example_2(self):
        s = "abBAcC"
        expected_output = ""
        self.assertEqual(make_good_string_v2(s), expected_output)
    
    def test_example_3(self):
        s = "s"
        expected_output = "s"
        self.assertEqual(make_good_string_v2(s), expected_output)
        
if __name__ == "__main__":
    unittest.main()