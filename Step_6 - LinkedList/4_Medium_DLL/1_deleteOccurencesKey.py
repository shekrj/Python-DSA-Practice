class Solution:
    def deleteAllOccurOfX(self, head, x):
        temp=head
        while temp:
            if temp.data==x:
                if temp==head:
                    head=head.next
                back=temp.prev
                front=temp.next
                if back:
                    back.next=front
                if front:
                    front.prev=back
                temp=temp.next
            else:
                temp=temp.next
        return head