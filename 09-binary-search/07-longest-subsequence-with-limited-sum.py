# Longest Subsequence With Limited Sum

# You are given 
#   an integer array nums of length n, 
#   and 
#   an integer array queries of length m.

# Return 
#   an array answer of length m 
# where 
#   answer[i] is the maximum size of a subsequence 
#       that you can take from nums 
#           such that the sum of its elements 
#               is less than or equal to queries[i].

# A subsequence is an array 
# that can be derived from another array 
# by deleting some or no elements 
# without changing the order of the remaining elements.

# Example
# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

# Constraints:
#    n == nums.length
#    m == queries.length
#    1 <= n, m <= 1000
#    1 <= nums[i], queries[i] <= 10^6


def get_longest_subsequence_with_limited_sum(nums: list[int], queries: list[int]) -> list[int]:
    
        def binary_search(items, target: int) -> int:
            left = 0
            right = len(items) - 1
                    
            while left <= right:
                mid = (left + right) // 2
                if items[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left

        
        nums.sort()
        answer : list[int] = []
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        for query in queries:
            ans = binary_search(nums, query)
            answer.append(ans)
        
        return answer


print(get_longest_subsequence_with_limited_sum([736411,184882,914641,37925,214915], [331244,273144,118983,118252,305688,718089,665450]))
print(get_longest_subsequence_with_limited_sum([4,5,2,1], [3,10,21]))
print(get_longest_subsequence_with_limited_sum([2,3,4,5], [1]))