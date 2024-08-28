# Given the head of a linked list 
# and an integer k, 
# return the k(th) node from the end.

# For example, 
# given the linked list that represents 
# 1 -> 2 -> 3 -> 4 -> 5 and k = 2, 
# return the node with value 4, 
# as it is the 2nd node from the end.


class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def find_node(head: LinkedListNode, k: int) -> LinkedListNode:
    slow = head
    fast = head

    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow


one = LinkedListNode(1)
two = LinkedListNode(2)
tree = LinkedListNode(3)
four = LinkedListNode(4)
five = LinkedListNode(5)
one.next = two
two.next = tree
tree.next = four
four.next = five



print(find_node(one, 1).val)