class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next

def add2(l1, l2):
    t1=l1
    t2=l2
    carry=0
    dummy=Node()
    temp=dummy

    while t1 or t2 or carry:
        totalsum=0
        if t1:
            totalsum+=t1.data
            t1=t1.next
        if t2:
            totalsum+=t2.data
            t2=t2.next
        totalsum+=carry
        carry=totalsum//10
        newnode=Node(totalsum%10)
        temp.next=newnode
        temp=temp.next
        
    return dummy.next