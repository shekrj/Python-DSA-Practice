class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
        
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

def deleteElement(head, el):
    if head is None:
        return head
    if head.data==el:
        return head.next
    
    temp=head
    prev=None
    while temp is not None:
        if temp.data==el:
            if prev is not None:
                prev.next=temp.next
            break
        prev=temp
        temp=temp.next
        
    return head