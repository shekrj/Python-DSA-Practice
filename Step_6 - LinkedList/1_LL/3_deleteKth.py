class Node:
    def __init__(self, data1, next1=None):
        self.data=data1
        self.next=next1
        
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

def deleteKth(head, k):
    if head is None:
        return head
    if k==1:
        return head.next
    
    cnt=1
    temp=head
    prev=None
    while temp is not None:
        if cnt==k:
            if prev is not None:
                prev.next=temp.next
            break
        prev=temp
        temp=temp.next
        cnt+=1
        
    return head