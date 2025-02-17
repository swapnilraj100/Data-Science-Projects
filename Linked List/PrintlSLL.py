class Node:
    def __init__(self,k):
        self.key = k
        self.next = None
def PrintList(head):
    curr = head
    while curr != None:
        print(curr.key,end=" ")
        curr = curr.next
temp = None
head = temp
PrintList(head)
