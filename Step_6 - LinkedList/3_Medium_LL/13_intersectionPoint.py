class Solution:    
    def yIntersection(self, head1, head2):
        temp1=head1
        temp2=head2
        while temp1!=temp2:
            if temp1 is not None:
                temp1=temp1.next
            else:
                temp1=head2
            if temp2 is not None:
                temp2=temp2.next
            else:
                temp2=head1
        return temp1
