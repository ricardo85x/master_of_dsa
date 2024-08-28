# Same Tree

# Given the roots of two binary trees p and q, check if they
# are the same tree. Two binary trees are the same tree if
# they are structurally identical and the nodes have the
# same values.


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


l2child7 = TreeNode(7)
r2child2 = TreeNode(2)
r2child1 = TreeNode(1)

l2child11 = TreeNode(11, left=l2child7, right=r2child2)
r2child13 = TreeNode(13)
r2child4_right = TreeNode(4, right=r2child1)

l2child4 = TreeNode(4, left=l2child11)
r2child8 = TreeNode(8, left=r2child13, right=r2child4_right)

root2 = TreeNode(5, left=l2child4, right=r2child8)

# The binary tree:
#
#                5
#              /   \
#             4     8
#            /    /  \
#           11  13    4
#          /  \        \
#         7    2        1                

def is_the_same(p: TreeNode, q: TreeNode) -> bool:

    if not p and not q:
        return True
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False

    left = is_the_same(p.left, q.left)
    right = is_the_same(p.right, q.right)

    return left and right
    

if is_the_same(root, root2):
    print("it is the same")
else:
    print("not the same")
