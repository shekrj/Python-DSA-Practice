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
        
def insertBeforeGivenNodeisneverhead(head, val, k):
    temp = head

    while temp is not None:
        if temp.data == k:  # Found the node with value k
            break
        temp = temp.next

    if temp is None or temp.back is None:  # If k is not found or k is the head (should never be)
        return head

    prev = temp.back
    newNode = Node(val, temp, prev)
    prev.next = newNode
    temp.back = newNode

    return head