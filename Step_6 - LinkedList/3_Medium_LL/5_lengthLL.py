

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                fast=fast.next
                cnt=1
                while fast!=slow:
                    fast=fast.next
                    cnt+=1
                return cnt
        return 0
        #Your code here