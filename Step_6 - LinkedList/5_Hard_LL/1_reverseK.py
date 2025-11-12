class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseLinkedList(self, head):
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def getKthNode(self, temp, k):
        k -= 1
        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        return temp
    def reverseKGroup(self, head, k):
        temp = head
        prevLast = None
        while temp is not None:
            kThNode = self.getKthNode(temp, k)
            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                    break
            nextNode = kThNode.next
            kThNode.next = None
            self.reverseLinkedList(temp)
            if temp == head:
                head = kThNode
            else:
                prevLast.next = kThNode
            prevLast = temp
            temp = nextNode
        return head
    


    def reverseKthGroups(self, head, k):
        if head is None:
            return None
        cnt=0
        temp=head
        while temp and cnt<k:
            cnt+=1
            temp=temp.next
        if cnt<k:
            return head
        temp=head
        prev=None
        for _ in range(k):
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        head.next=self.reverseKthGroups(temp, k)
        return prev
            