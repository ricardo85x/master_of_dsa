# Group Anagrams

# Given an array of strings strs, 
# group the anagrams together.

# For example, 
# given strs = ["eat","tea","tan","ate","nat","bat"], 
# return [["bat"],["nat","tan"],["ate","eat","tea"]].

from collections import defaultdict
def group_anagram(strs: list[str]) -> list[list[str]]:
    group = defaultdict(list)
    
    for s in strs:
        key = "".join(sorted(s))
        group[key].append(s)
        
    return list(group.values())

def group_anagram_v2(strs: list[str]) -> list[list[str]]:
    group = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        group[key].append(s)
    return list(group.values())


import unittest

def sort_groups(anagrams):
    return sorted([sorted(group) for group in anagrams])

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected_output = [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        result = group_anagram_v2(strs)
        self.assertEqual(sort_groups(result), sort_groups(expected_output))
        
    def test_example_2(self):
        strs = ["abc", "bca", "cab", "xyz", "zyx", "zxy"]
        expected_output = [["abc", "bca", "cab"], ["xyz", "zyx", "zxy"]]
        
        result = group_anagram_v2(strs)
        self.assertEqual(sort_groups(result), sort_groups(expected_output))
    
    def test_example_3(self):
        strs = ["listen", "silent", "enlist", "google", "gogole", "inlets"]
        expected_output = [["listen", "silent", "enlist", "inlets"], ["google", "gogole"]]
        
        result = group_anagram_v2(strs)
        self.assertEqual(sort_groups(result), sort_groups(expected_output))
                
if __name__ == "__main__":
    unittest.main()
    

    