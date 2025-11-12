class Node:
    def __init__(self, val=0, next=None, rand=None):
        self.val=val
        self.next=next
        self.rand=rand
        
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        oldToNew={}
        temp=head
        while temp:
            copy=Node(temp.val)
            oldToNew[temp]=copy
            temp=temp.next
        
        temp=head
        while temp:
            copy=oldToNew[temp]
            copy.next=oldToNew[temp.next] if temp.next else None
            copy.random=oldToNew[temp.random] if temp.random else None
            temp=temp.next
        return oldToNew[head]