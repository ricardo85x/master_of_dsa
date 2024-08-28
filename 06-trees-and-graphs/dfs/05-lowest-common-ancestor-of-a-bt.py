# Lowest Common Ancestor of a Binary Tree

# Given the root of a binary tree and two nodes p and q that
# are in the tree, return the lowest common ancestor (LCA)
# of the two nodes. The LCA is the lowest node in the tree
# that has both p and q as descendants (note: a node is a
# descendant of itself).

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


def get_lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

    if not root:
        return None

    if root == p or root == q:
        return root

    left = get_lca(root.left, p, q)
    right = get_lca(root.right, p, q)

    if left and right:
        return root
    
    if left:
        return left

    return right

lca_node = get_lca(root, rchild13, rchild1)

if lca_node:
    print(lca_node.val)
else:
    print("not found")