from PrintlSLL import Node, PrintList
def insertEnd(head,key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head
head = None
head = insertEnd(head,10)
head = insertEnd(head,21)
head = insertEnd(head,30)
PrintList(head)