from PrintlSLL import PrintList, Node
def search(head,x):
    pos = 1
    curr = head
    while curr != None:
        if curr.key == x:
            return pos
        pos += 1
        curr = curr.next
    return -1 
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(30)
print(search(head,30))