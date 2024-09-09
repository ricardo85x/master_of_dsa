# Number of Provinces

# There are n cities. 
# A province is a group of directly 
# or indirectly connected cities 
# and no other cities outside of the group. 
# 
# You are given an n x n matrix isConnected 
#   where 
#       isConnected[i][j] = isConnected[j][i] = 1 
#           if the i(th) city and 
#               the j(th) city 
#                   are directly connected, 
#       and isConnected[i][j] = 0 
#           otherwise. 
#  Return the total number of provinces.

from collections import defaultdict

def get_number_of_provinces(isConnected: list[list[int]]) -> int:
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    n = len(isConnected)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
                print("i ", i, "j", j, "is", isConnected[i][j])

    # updated graph           
    # {
    #   1: [2, 7], 
    #   2: [1, 4], 
    #   7: [1], 
    #   4: [2], 
    #   5: [6], 
    #   6: [5]
    # }
    
    seen = set()
    result = 0

    for i in range(n):
        if i not in seen:
            result += 1
            seen.add(i)
            dfs(i)
            
    return result

# Example input:
#    0      1        4    5
#          / \      /      \
#         7   3    2        6
 
isConnected = [
   [1, 0, 0, 0, 0, 0, 0, 0],  # Node 0
   [0, 1, 1, 0, 0, 0, 0, 1],  # Node 1
   [0, 0, 1, 0, 1, 0, 0, 0],  # Node 2
   [0, 1, 0, 1, 0, 0, 0, 0],  # Node 3
   [0, 0, 1, 0, 1, 0, 0, 0],  # Node 4
   [0, 0, 0, 0, 0, 1, 1, 0],  # Node 5
   [0, 0, 0, 0, 0, 1, 1, 0],  # Node 6
   [0, 1, 0, 0, 0, 0, 0, 1]   # Node 7
]

print(get_number_of_provinces(isConnected))  
# Output: 4

