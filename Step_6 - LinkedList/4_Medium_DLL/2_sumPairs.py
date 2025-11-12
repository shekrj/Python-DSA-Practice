class Solution:
    def findPairsWithGivenSum(self, target, head):
        result = []
        start = head
    
    # Move to the end to set the end pointer
        end = head
        while end.next:
            end = end.next

    # Two-pointer approach
        while start != end and start.prev != end:
            s = start.data + end.data
            if s == target:
                result.append((start.data, end.data))
                start = start.next
                end = end.prev
            elif s < target:
                start = start.next
            else:
                end = end.prev

        return result
        