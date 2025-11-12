class Node:
    def __init__(self, data, next=None, back=None):
        self.data=data
        self.next=next
        self.back=back
def converARRtoDLL(arr):
    if not arr:
        return None
    head=Node(arr[0])
    prev=head
    
    for i in range(1, len(arr)):
         temp=Node(arr[i])
         prev.next=temp
         temp.back=prev
         prev=temp

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

def insertTail(head, val):
    if head is None or head.next is None:  # If DLL has 0 or 1 node, insert at head
        return Node(val, head, None) if head is None else Node(val, head, None)
    tail=head
    while tail.next is not None:
        tail=tail.next
    prev=tail.back
    newNode=Node(val, tail, prev)
    prev.next=newNode
    tail.back=newNode
    return head