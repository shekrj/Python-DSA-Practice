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
def insertHeadbefore(head, val):
    newhead=Node(val, head, None)
    if head is not None:
        head.back=newhead
    return newhead
    