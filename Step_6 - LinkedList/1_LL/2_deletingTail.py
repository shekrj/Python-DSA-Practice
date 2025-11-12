class Node:
    def __init__(self, data1, next1=None):
        self.data=data1
        self.next=next1
        
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

def removesTail(head):
    if head==None or head.next==None:
        return None
    
    temp=head
    while temp.next.next!=None:
        temp=temp.next
        
    temp.next=None
    return head
