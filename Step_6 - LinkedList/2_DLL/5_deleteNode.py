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

def deleteNodeWhileNodeIsNeverHead(temp):
    prev=temp.back
    front=temp.next
    if front is None:
        prev.next=None
        temp.back=None
        return
    prev.next=front
    front.back=prev
    temp.next=temp.back=None