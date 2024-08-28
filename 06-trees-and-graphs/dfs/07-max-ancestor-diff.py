# Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the maximum value v
# for which there exist different nodes a and b where
# v = |a.val - b.val| and a is an ancestor of b.
#
# A node a is an ancestor of b if either: any child of a is
# equal to b or any child of a is an ancestor of b.


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

root = TreeNode(6, left=lchild1, right=rchild2)

# The binary tree:
#
#                6
#              /   \
#             1     2
#            / \     \
#           3   4     5
#                \
#                 6

def get_max_ancestor(root: TreeNode):

    max_value = 0
    def dfs(node: TreeNode, ancestors: list[int]):
        nonlocal max_value

        if not node:
            return
        print(node.val)
        for i in ancestors:
            max_value = max(max_value, abs(i - node.val))

        ancestors.append(node.val)

        dfs(node.left, ancestors)
        dfs(node.right, ancestors)

        ancestors.pop()

    dfs(root, [])
    return max_value
    
print("Max ancestor diff", get_max_ancestor(root))