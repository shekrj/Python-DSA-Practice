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

def deleteKth(head, k):
    if head is None:  # Case 1: Empty list
        return None

    temp = head
    cnt = 1

    while temp is not None and cnt < k:  # Traverse to the Kth node
        temp = temp.next
        cnt += 1

    if temp is None:  # Case 2: k is out of bounds
        return head

    prev = temp.back
    front = temp.next

    if prev is None and front is None:  # Case 3: Only one node in the list
        return None
    elif prev is None:  # Case 4: Deleting the head
        head = head.next
        head.back = None
    elif front is None:  # Case 5: Deleting the tail
        prev.next = None
    else:  # Case 6: Deleting a middle node
        prev.next = front
        front.back = prev
        
    return head