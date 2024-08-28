# Find Largest Value in Each Tree Row

# Given the root of a binary tree, return an array of the
# largest value in each row of the tree.


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


def largest_value(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        nodes_size = len(queue)
        
        max_value = float('-inf')

        for _ in range(nodes_size):
            node = queue.popleft()

            max_value = max(max_value, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(max_value)

    return result
    

print(largest_value(root))