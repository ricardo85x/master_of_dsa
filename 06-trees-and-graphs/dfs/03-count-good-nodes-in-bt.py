# Count Good Nodes in Binary Tree

# Given the root of a binary tree, 
# find the number of nodes that are good. 
# A node is good if the path between the root
# and the node has no nodes with a greater value.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


lchild7 = TreeNode(7)
rchild2 = TreeNode(2)
rchild1 = TreeNode(1)

lchild11 = TreeNode(11, left=lchild7, right=rchild2)
rchild13 = TreeNode(13)
rchild4_right = TreeNode(4, right=rchild1)

lchild4 = TreeNode(4, left=lchild11)
rchild8 = TreeNode(8, left=rchild13, right=rchild4_right)

root = TreeNode(5, left=lchild4, right=rchild8)

# The binary tree:
#
#                5
#              /   \
#             4     8
#            /    /  \
#           11  13    4
#          /  \        \
#         7    2        1                

def good_nodes(root: TreeNode) -> int:
    gnCount = 0
    def dfs(node: TreeNode, curMax: int) -> int:
        nonlocal gnCount

        if not node:
            return
        
        if node.val > curMax:
            curMax = node.val
            gnCount += 1
        
        if node.left:
            dfs(node.left, curMax=curMax)
        if node.right:
            dfs(node.right, curMax=curMax)
        
    dfs(root, curMax=float('-inf'))
    return gnCount

print(good_nodes(root))
