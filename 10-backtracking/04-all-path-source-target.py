# All Paths From Source to Target

# Given a 
# directed acyclic graph (DAG)
# of n nodes labeled from 0 to n - 1, 
# find all possible paths from node 0 to node n - 1 
# and return them in any order.


# The graph is given as follows: 
# graph[i] is a list of all nodes you can visit from node i 
# (i.e., there is a directed edge from node i to node graph[i][j]).

# Ex
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Ex 2
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

# Constraints:
#   n == graph.length
#   2 <= n <= 15
#   0 <= graph[i][j] < n
#   graph[i][j] != i (i.e., there will be no self-loops).
#   All the elements of graph[i] are unique.
#   The input graph is guaranteed to be a DAG.

def all_path_source_target(graph: list[list[int]]) -> list[list[int]]:
    
    target = len(graph) - 1
    results = []
    def backtrack(curr_node, path):
        if curr_node == target:
            results.append(list(path))
            return
        for next_node in graph[curr_node]:
            path.append(next_node)
            backtrack(next_node, path)
            path.pop()
        
    path = [0]
    backtrack(0, path)
    return results

print(all_path_source_target([[1,2],[3],[3],[]]))