# DFS sample recursion

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


lchild6 = TreeNode(6)

lchild3 = TreeNode(3)
rchild4 = TreeNode(4, right=lchild6)

rchild5 = TreeNode(5)

lchild1 = TreeNode(1, left=lchild3, right=rchild4)
rchild2 = TreeNode(2, right=rchild5)

root = TreeNode(0, left=lchild1, right=rchild2)

# The binary tree:
#
#                0
#              /   \
#             1     2
#            / \     \
#           3   4     5
#                \
#                 6


def inorder_dfs(node: TreeNode):
    if node == None:
        return
    
    inorder_dfs(node.left)
    print("Node ", node.val)
    inorder_dfs(node.right)
    return


inorder_dfs(root)
