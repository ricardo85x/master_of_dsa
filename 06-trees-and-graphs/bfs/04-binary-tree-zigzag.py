# Binary Tree Zigzag Level Order Traversal

# Given the root of a binary tree, 

# return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def lst_to_tree(lst) -> TreeNode: 
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    for i, node in enumerate(nodes):
        if node:
            if 2 * i + 1 < len(nodes):
                node.left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                node.right = nodes[2 * i + 2]
    return nodes[0]


def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    result = []
    if not root:
        return result
    
    queue = deque([root])
    left_to_right = True  
    
    while queue:
        cur_num_nodes = len(queue)
        level = deque()

        for _ in range(cur_num_nodes):
            node = queue.popleft()
            
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(list(level))     
        left_to_right = not left_to_right
        
    return result



import unittest

class TestDSA(unittest.TestCase):
    
    def test_example_1(self):
        root = [3,9,20,None,None,15,7]
        root_tree = lst_to_tree(root)
        expected_output = [[3],[20,9],[15,7]]
        self.assertEqual(zigzagLevelOrder(root_tree), expected_output)
        
    def test_example_2(self):
        root = [1]
        root_tree = lst_to_tree(root)
        expected_output = [[1]]
        self.assertEqual(zigzagLevelOrder(root_tree), expected_output)

    def test_example_3(self):
        root = []
        root_tree = lst_to_tree(root)
        expected_output = []
        self.assertEqual(zigzagLevelOrder(root_tree), expected_output)

    def test_example_4(self):
        root = [1,2,3,4,None,None,5]
        root_tree = lst_to_tree(root)
        expected_output = [[1],[3,2],[4,5]]
        self.assertEqual(zigzagLevelOrder(root_tree), expected_output)
        
if __name__ == "__main__":
    unittest.main()