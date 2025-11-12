class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev
    
    def insertCDLL(self, head, newNode, k):
        if not head:
            return newNode
        temp=head
        while temp.next!=head:
            temp=temp.next
        temp.next=newNode
        newNode.prev=temp
        newNode.next=head
        head.prev=newNode
        return head
    
    def delete(self, head, x):
        if head.val==x.val:
            if head.next==head:
                return None
            else:
                temp=head
                while temp.next!=head:
                    temp=temp.next
                last=temp
                last.next=head.next
                head.next.prev=last
                return head.next
        temp=head
        while temp.next != head:
            temp=temp.next
            if temp.val==x.val:
                back=temp.prev
                front=temp.next
                back.next=front
                front.prev=back
        return head
    