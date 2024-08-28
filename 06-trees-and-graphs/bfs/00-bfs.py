# example BFS

from collections import deque
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


def print_all_nodes(root: TreeNode):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        for _ in range(nodes_in_current_level):
            node = queue.popleft()
            print("n nodes", nodes_in_current_level, " value", node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

print_all_nodes(root)