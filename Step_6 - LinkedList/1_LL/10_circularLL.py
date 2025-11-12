class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
    
    def insertInACircularLL(self, head, newNode):
        if head is None:
            newNode.next=newNode
            return newNode
        
        temp=head        
        while temp.next!=head:
            temp=temp.next

        temp.next=newNode
        newNode.next=temp
        return head

    def delete(self, head, x):
        if not head:
            return None
        if head.val==x.val:
            if head.next==head:
                head.next=None
                return None
            else:
                newHead=head.next
                head.next=None
                return newHead
        temp=head.next
        prev=head
        while temp.next!=head:
            front=temp.next
            if temp.val==x.val:
                prev.next=front
                temp.next=None
            prev=temp
            temp=temp.next
        return head      