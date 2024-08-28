# Maximum Depth of Binary Tree

# Given the root of a binary tree, 
# find the length of the longest path from the root to a leaf.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


lchild3 = TreeNode(3)

lchild1 = TreeNode(1, left=lchild3)
rchild2 = TreeNode(2)

root = TreeNode(0, left=lchild1, right=rchild2)

# The binary tree:
#
#                0
#              /   \
#             1     2
#            /      
#           3        
#                      

def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    
    stack = [(root, 1)]
    ans = 0

    while stack:
        node, depth = stack.pop()
        ans = max(ans, depth)
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    
    return ans

print(max_depth(root))
    

