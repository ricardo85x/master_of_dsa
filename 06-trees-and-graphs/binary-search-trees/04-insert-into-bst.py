# Insert into a Binary Search Tree

# You are given the root node 
# of a binary search tree (BST) 
# and a value to insert into the tree. 
# Return the root node of the BST 
# after the insertion. 
# It is guaranteed that the new value 
# does not exist in the original BST.
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node12 = TreeNode(12)
node35 = TreeNode(35)
node68 = TreeNode(68)
node84 = TreeNode(84)

node24 = TreeNode(24, left=node12, right=node35)
node60 = TreeNode(60, right=node68)
node72 = TreeNode(72, left=node60, right=node84)

root = TreeNode(48, left=node24, right=node72)

# The binary search tree:
#
#                48
#              /    \
#            24      72
#           /  \    /  \
#          12  35  60  84
#                   \
#                    68

def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert_into_bst(root.right, val)
    else:
        root.left = insert_into_bst(root.left, val)
    return root


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


print_all_nodes(insert_into_bst(root, 49))

# Result:
#
#                48
#              /    \
#            24      72
#           /  \    /  \
#          12  35  60  84
#                 /  \
#                49   68