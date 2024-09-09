# Permutations

# Given an array nums of distinct integers, 
# return all the possible permutations in any order.

# For example, 
# given nums = [1, 2, 3], 
# return [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ].

def permute(nums: list[int]) -> list[list[int]]:
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        
        for num in nums:
            if num not in ans:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    ans = []
    backtrack([])
    return ans

print(permute([1,2]))