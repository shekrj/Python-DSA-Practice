class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):  # Iterate until the last possible match position
            if haystack[i:i + m] == needle:  # Check substring match
                return i
        
        return -1  # Pattern not found

        