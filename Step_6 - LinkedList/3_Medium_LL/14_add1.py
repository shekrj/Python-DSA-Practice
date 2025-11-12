class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reversal(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

def addOne(head):                                                                       
    head = reversal(head)
    carry = 1
    temp = head
    while temp:
        temp.data += carry
        carry = temp.data // 10
        temp.data %= 10

        if not temp.next and carry:
            temp.next = Node(carry)
            break

        temp = temp.next
        
    return reversal(head)