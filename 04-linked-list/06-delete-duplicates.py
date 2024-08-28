# Remove Duplicates from Sorted List

# Given the head of a sorted linked list, 
# delete all duplicates such that 
# each element appears only once. 
# 
# Return the linked list sorted as well.

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def createLinkedList(size: int, start_at = 1) -> LinkedListNode:
    head = None
    tail = None
    for i in range(start_at, size + 1):
        current = LinkedListNode(i)
        if head is None:
            head = current
        else:
            tail.next = current
        tail = current

    return head


def remove_duplicates_from_sorted(head: LinkedListNode) -> LinkedListNode:
    current = head

    while current and current.next:
        if current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


head = createLinkedList(3, 1)
duplicated = LinkedListNode(3)
head.next.next.next = duplicated
four = LinkedListNode(4)
head.next.next.next.next = four

# print(head.next.next.next.next.val)

no_duplication = remove_duplicates_from_sorted(head)
print(no_duplication.next.next.next.next)
print(head.next.next.next.next)
