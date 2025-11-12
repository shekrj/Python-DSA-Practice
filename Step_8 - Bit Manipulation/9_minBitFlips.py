class Solution(object):
    def minBitFlips(self, start, goal):
        xor = start ^ goal
        count = 0
        while xor:
            if xor & 1:
                count += 1
            xor >>= 1
        return count