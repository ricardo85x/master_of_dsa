# Validate Binary Search Tree

# Given the root of a binary tree, 
# determine if it is a valid BST.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node12 = TreeNode(12)
node35 = TreeNode(35)
node68 = TreeNode(68)
node84 = TreeNode(84)

node24 = TreeNode(24, left=node12, right=node35)
node60 = TreeNode(60, right=node68)
node72 = TreeNode(72, left=node60, right=node84)

root = TreeNode(48, left=node24, right=node72)

# The binary search tree:
#
#                48
#              /    \
#            24      72
#           /  \    /  \
#          12  35  60  84
#                   \
#                    68


def validate_bst(root: TreeNode) -> int:
    def dfs(node: TreeNode, small: int, large: int) -> bool:
        if not node:
            return True
        
        if not (small < node.val < large):
            return False
        
        left = dfs(node.left, small, node.val)
        right = dfs(node.right, node.val, large)

        return left and right
    return dfs(root, float('-inf'), float('inf'))


print(validate_bst(root))