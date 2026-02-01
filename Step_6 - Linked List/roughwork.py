class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
    
class Solution:
    def revLL(self, head: Node) -> Node:
        if not head:
            return None
        temp=head
        prev=None
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    
    def revDLL(self, head: Node) -> Node:
        if not head:
            return None
        temp=head
        newHead=None
        while temp:
            temp.prev, temp.next=temp.next, temp.prev
            newHead=temp
            temp=temp.prev
        return newHead
    
    def lengthOfLoop(self, head: Node) -> int:
        if not head:
            return 0
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=slow.next
                cnt=1
                while slow!=fast:
                    slow=slow.next
                    cnt+=1
                return cnt
        return 0