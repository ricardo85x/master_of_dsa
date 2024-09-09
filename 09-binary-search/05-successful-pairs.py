# Successful Pairs of Spells and Potions

# You are given two positive integer arrays 
#   spells and potions, 
# where spells[i] 
#   represents the strength of the i^th spell 
# and potions[j] 
#   represents the strength of the j^th potion.
# You are also given an 
#   integer success. 

# A spell and potion pair is considered successful 
#   if the product of their strengths 
#       is at least success. 

# For each spell, 
#   find how many potions 
#       it can pair with to be successful. 
# Return an integer array 
#   where the i^th element 
#       is the answer for the i^th spell.


def successful_pairs(spells: list[int], potions: list[int], success: int) -> list[int]:

    def binary_search(items: list[int], target: int) -> int:
        left = 0
        right = len(items) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if items[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    potions.sort()
    ans = []
    m = len(potions)
    
    for spell in spells:
        i = binary_search(potions, success / spell)
        ans.append(m - i)
    return ans
        
spells = [1,2,3,4,5]
potions = [5,1,3]
success = 7

print(successful_pairs(spells, potions, success))