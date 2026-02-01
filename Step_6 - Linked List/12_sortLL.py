class Solution:
    def sortLL(self, head):
        if head is None or head.next is None:
            return head
        temp=head
        arr1=[]
        while temp:
            arr1.append(temp.val)
            temp=temp.next
        arr1.sort()
        temp=head
        i=0
        while temp:
            temp.val=arr1[i]
            i+=1
            temp=temp.next
        return head