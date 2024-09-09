# Combinations

# Given two integers n and k, 
# return 
#   all combinations of k numbers 
#       out of the range [1, n] 
#   in any order.

# For example, 
# given 
#   n = 4, 
#   k = 2, 
# return [
#   [2,4],[3,4],[2,3],[1,2],[1,3],[1,4]
# ].

def combinations(n: int, k: int) -> list[list[int]]:
    def backtrack(curr, i):
        if len(curr) == k:
            ans.append(curr[:])
            return
   
        for num in range(i, n + 1):
            curr.append(num)
            backtrack(curr, num + 1)
            curr.pop()
    
    ans = []
    backtrack([], 1)
    return ans

print(combinations(4, 2))