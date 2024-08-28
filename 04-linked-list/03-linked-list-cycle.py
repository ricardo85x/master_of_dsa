# Linked List Cycle

# Given the head of a linked list, 
# determine if the linked list has a cycle.

# There is a cycle in a linked list 
# if there is some node in the list 
# that can be reached again by continuously 
# following the next pointer.

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head: LinkedListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False


one = LinkedListNode(1)
two = LinkedListNode(2)
tree = LinkedListNode(3)
four = LinkedListNode(4)
five = LinkedListNode(5)
one.next = two
two.next = tree
tree.next = four
four.next = five

five.next = one


if has_cycle(one):
    print("Has cicle")
else:
    print("Does not have a cicle")