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

def insertBeforeKth(head, val, k):
    if head is None or k <= 1:  # If DLL is empty or inserting before head
        newNode = Node(val, head, None)
        if head:
            head.back = newNode
        return newNode

    temp = head
    cnt = 1
    
    while temp is not None:
        if cnt == k:  # Found the k-th node
            break
        temp = temp.next
        cnt += 1

    if temp is None:  # If k is out of range (greater than length of DLL)
        return head

    prev = temp.back
    newNode = Node(val, temp, prev)
    prev.next = newNode
    temp.back = newNode
    
    return head