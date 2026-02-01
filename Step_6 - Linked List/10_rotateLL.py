class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        cnt=1
        temp=head
        while temp.next:
            cnt+=1
            temp=temp.next
        temp.next=head
        k=k%cnt
        stepsToNewTail=cnt-k-1
        temp=head
        while stepsToNewTail!=0:
            temp=temp.next
            stepsToNewTail-=1
        newHead=temp.next
        temp.next=None
        return newHead