from PrintlSLL import Node,PrintList
def reverseList(head):
    curr = head
    prev = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(30)
PrintList(head)
print()
head = reverseList(head)
PrintList(head)