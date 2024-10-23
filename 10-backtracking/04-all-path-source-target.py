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
    result = []
    
    def backtrack(curr: int, paths: list[int]):
        if curr == target:
            result.append(paths[:])
            return
        for new_node in graph[curr]:
            paths.append(new_node)
            backtrack(new_node, paths)
            paths.pop()
        
    backtrack(0, [0])
    return result

import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        graph = [[1,2],[3],[3],[]]
        expected_output = [[0,1,3],[0,2,3]]
        self.assertEqual(all_path_source_target(graph), expected_output)
        
    def test_example_2(self):
        graph = [[4,3,1],[3,2,4],[3],[4],[]]
        expected_output = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
        self.assertEqual(all_path_source_target(graph), expected_output)
 
if __name__ == "__main__":
    unittest.main()