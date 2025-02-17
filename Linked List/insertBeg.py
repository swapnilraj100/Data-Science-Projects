from PrintlSLL import PrintList, Node
def insertBegin(head,key):
    temp = Node(key)
    temp.next = head
    return temp
head = None
head = insertBegin(head,10)
head = insertBegin(head,21)
head = insertBegin(head,30)
PrintList(head)