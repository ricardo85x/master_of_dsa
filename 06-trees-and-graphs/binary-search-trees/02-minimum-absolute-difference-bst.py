# Minimum Absolute Difference in BST

# Given the root of a BST, 
# return the minimum absolute difference 
# between the values of any two different nodes 
# in the tree.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node12 = TreeNode(12)
node36 = TreeNode(36)
node68 = TreeNode(68)
node84 = TreeNode(84)

node24 = TreeNode(24, left=node12, right=node36)
node60 = TreeNode(60, right=node68)
node72 = TreeNode(72, left=node60, right=node84)

root = TreeNode(48, left=node24, right=node72)

# The binary search tree:
#
#                48
#              /    \
#            24      72
#           /  \    /  \
#          12  36  60  84
#                   \
#                   68


def min_abs_diff(root: TreeNode) -> int:
    prev = None
    result = float('inf')

    def dfs(node: TreeNode):
        nonlocal result, prev

        if not node:
            return
        
        dfs(node.left)
        if prev is not None:
            result = min(result, node.val - prev)
        prev = node.val
        dfs(node.right)
    
    dfs(root)
    return result

print(min_abs_diff(root))