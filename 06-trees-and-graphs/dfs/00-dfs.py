# DFS sample recursion

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


lchild6 = TreeNode(6)
lchild7 = TreeNode(7)
rchild8 = TreeNode(8)

lchild3 = TreeNode(3,left=lchild6)
rchild4 = TreeNode(4, left=lchild7, right=rchild8)

rchild5 = TreeNode(5)

rchild2 = TreeNode(2, right=rchild5)
lchild1 = TreeNode(1, left=lchild3,right=rchild4)

root = TreeNode(0, left=lchild1, right=rchild2)

# The binary tree:
#
#                0
#              /   \
#             1     2
#            / \     \
#           3   4     5
#          /   / \
#         6   7   8


def dfs(node: TreeNode):
    if node == None:
        return
    
    dfs(node.left)
    dfs(node.right)
    print("Node ", node.val)
    return


dfs(root)
