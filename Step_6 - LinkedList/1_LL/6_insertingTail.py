class Node:
    def __init__(self, data1, next1=None):
        self.data=data1
        self.next=next1
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
def insertTail(head, value):
    if head is None:
        return Node(value)
    temp=head
    while temp.next is not None:
        temp=temp.next
    Node(value)
    


    return head