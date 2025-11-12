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

        
def insertHeadAfter(head, val):
    if head is None:  # If list is empty, just return a new node
        return Node(val)

    new_node = Node(val, head.next, head)  # Create new node
    if head.next is not None:  # If head has a next node, update its back pointer
        head.next.back = new_node
    head.next = new_node  # Link head to new node

    return head