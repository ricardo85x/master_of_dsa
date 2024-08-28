# Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the
# shortest path from the root node down to the nearest
# leaf node.
#
# Note: A leaf is a node with no children.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

lchild7 = TreeNode(7)
rchild6 = TreeNode(6)

lchild5 = TreeNode(5, left=lchild7)
rchild4 = TreeNode(4, right=rchild6)

lchild3 = TreeNode(3, left=lchild5)
rchild2 = TreeNode(2, right=rchild4)

lchild1 = TreeNode(1, left=lchild3)

root = TreeNode(0, left=lchild1, right=rchild2)

# The binary tree:
#
#                0
#              /   \
#             1     2
#            /       \ 
#           3         4
#          /           \
#         5             6
#        /
#       7

def min_depth(root: TreeNode) -> int:

    minDepth = float('inf')
    def dfs(node: TreeNode, curDepth: int):
        nonlocal minDepth
        if not node:
            return
        curDepth += 1
        if not node.left and not node.right:
           if curDepth < minDepth:
                minDepth = curDepth

        dfs(node.left, curDepth)
        dfs(node.right, curDepth)
    
    dfs(root, 0)
    return minDepth
        
print(min_depth(root))