class Solution:
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is now at the middle node
        # prev is the node before slow
        prev.next = slow.next

        return head