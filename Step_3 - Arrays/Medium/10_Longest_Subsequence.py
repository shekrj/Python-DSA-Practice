from typing import List

def longest_successive_elements(a: List[int]) -> int:
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set(a)  # Put all elements into a set for quick lookups

    # Find the longest sequence
    for i in st:
        # Check if it's the start of a sequence
        if i - 1 not in st:
            cnt = 1
            x = i
            while x + 1 in st:
                x += 1
                cnt += 1
            
            longest = max(longest, cnt)
    
    return longest
