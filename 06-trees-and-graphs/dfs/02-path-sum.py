# Path Sum

# Given the root of a binary tree and an integer targetSum,
# return true if there exists a path from the root to a leaf
# such that the sum of the nodes on the path is equal to
# targetSum, and return false otherwise.

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

def has_path_sum(root: TreeNode, targetSum: int) -> bool:
    def dfs(node: TreeNode, curr: int):
        if not node:
            return False

        curr += node.val

        if not node.left and not node.right and curr == targetSum:
            return True

        return dfs(node.left, curr) or dfs(node.right, curr)
    
    return dfs(root, 0)
    

if has_path_sum(root, 22):
    print("Bingo")
else:
    print("Marmelada")