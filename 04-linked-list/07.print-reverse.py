# Reverse print


class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_print(head: LinkedListNode):
    
    def process(node: LinkedListNode):
        if node.next:
            process(node.next)
        print(node.val)
    
    process(head)
    

one = LinkedListNode(1)
two = LinkedListNode(2)
tree = LinkedListNode(3)
four = LinkedListNode(4)
five = LinkedListNode(5)
one.next = two
two.next = tree
tree.next = four
four.next = five

reverse_print(one)

