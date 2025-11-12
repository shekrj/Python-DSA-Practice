class Node:
    def __init__(self, x=None, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode
        
def flattenLinkedList(head):
    arr = []
    while head:
        t2 = head
        while t2:
            arr.append(t2.data)
            t2 = t2.child
        head = head.next
    arr.sort()
    return convertArrToLinkedList(arr)

def convertArrToLinkedList(arr):
    dummyNode = Node(-1)
    temp = dummyNode
    for i in arr:
        temp.child = Node(i)
        temp = temp.child
    return dummyNode.child