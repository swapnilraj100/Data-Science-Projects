from PrintlSLL import Node,PrintList
def insertPos(head,data,pos):
    temp = Node(data)
    if pos == 1:
        temp.next = head
        return temp
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = temp
    return head
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(1000)
PrintList(head)
print()
insertPos(head,1500,3)
PrintList(head)