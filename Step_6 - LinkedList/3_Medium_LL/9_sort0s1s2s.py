class Node:
	def __init__(self, data):   # data -> value stored in node
		self.data = data
		self.next = None
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if not head or not head.next:
            return head
        
        # Dummy nodes to store 0s, 1s, and 2s separately
        zeroD = Node(0)
        oneD = Node(0)
        twoD = Node(0)
        
        # Pointers to move along respective lists
        zero = zeroD
        one = oneD
        two = twoD
        
        current = head
        
        # Traverse and distribute nodes into separate lists
        while current:
            if current.data == 0:
                zero.next = current
                zero = zero.next
            elif current.data == 1:
                one.next = current
                one = one.next
            else:
                two.next = current
                two = two.next
            current = current.next
        
        # Connect the three lists
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None  # End the last node
        
        return zeroD.next