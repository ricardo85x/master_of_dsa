# Range Sum of BST

# Given the root node of a binary search tree and two
# integers low and high, return the sum of values of all
# nodes with a value in the inclusive range [low, high].

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node15 = TreeNode(15)
node65 = TreeNode(65)

node10 = TreeNode(10, right=node15)
node30 = TreeNode(30)
node60 = TreeNode(60, right=node65)
node80 = TreeNode(80)

node25 = TreeNode(25, left=node10, right=node30)
node75 = TreeNode(75, left=node60, right=node80)

root = TreeNode(50, left=node25, right=node75)

# The binary search tree:
#
#                50
#              /    \
#            25      75
#           /  \    /  \
#         10   30  60  80
#           \        \
#           15       65

def range_sum_bst(root: TreeNode, low: int, high: int) -> int:
    if not root:
        return 0

    result = 0
    if low <= root.val <= high:
        result += root.val
    
    if low < root.val:
        result += range_sum_bst(root.left, low, high)
    
    if root.val < high:
        result += range_sum_bst(root.right, low, high)
    
    return result

print(range_sum_bst(root, 10, 25))