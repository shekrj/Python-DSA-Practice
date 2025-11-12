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

def reverseDLL(head):
    temp=head
    new_head=None
    while temp is not None:
        temp.prev, temp.next = temp.next, temp. prev
        new_head=temp
        temp=temp.prev
    return new_head