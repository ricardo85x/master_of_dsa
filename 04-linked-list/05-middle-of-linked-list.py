#   Middle of the Linked List

# Given the head of a singly linked list, 
# return the middle node of the linked list.

# If there are two middle nodes, 
# return the second middle node.

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def createLinkedList(size: int) -> LinkedListNode:
    head = None
    tail = None
    for i in range(1, size + 1):
        current = LinkedListNode(i)
        if head is None:
            head = current
        else:
            tail.next = current
        tail = current

    return head


def middle_node(head: LinkedListNode) -> LinkedListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
        

head = createLinkedList(5)

print(middle_node(head).val)
