# Given the head of a linked list 
# with an odd number of nodes head, 
# return the value of the node in the middle.

# For example, 
# given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, 
# return 3.



class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_middle(head: LinkedListNode) -> int:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

one = LinkedListNode(1)
two = LinkedListNode(2)
tree = LinkedListNode(3)
four = LinkedListNode(4)
five = LinkedListNode(5)
one.next = two
two.next = tree
tree.next = four
four.next = five

print(get_middle(one))

