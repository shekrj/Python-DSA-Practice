class Node:
    def __init__(self, data1, next1=None):
        self.data=data1
        self.next=next1
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
def insertKth(head, value, k):
    if head is None:
        if k==1:    
            return Node(value)
        else:
            return None
    if k==1:
        return Node(value, head)
    cnt=1
    temp=head
    while temp is not None:
        if cnt==k-1:
            x=Node(value, temp.next)
            temp.next=x
            break
        temp=temp.next
        cnt+=1
    return head