# Deepest Leaves Sum

# Given the root of a binary tree, 
# return the sum of values of its deepest leaves. 

from collections import deque
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

def depest_leaves_sum(root: TreeNode) -> int:

    if not root:
        return None
    
    queue = deque([root])
    result = float("-inf")
    while queue:
        node_count = len(queue)
        level_sum = 0
        for _ in range(node_count):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result = level_sum
    return result

print(depest_leaves_sum(root))
        