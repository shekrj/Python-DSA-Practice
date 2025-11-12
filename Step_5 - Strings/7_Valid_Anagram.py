# SORT APPROACH
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

# MANUAL COUNTER ARRAY HASHING APPROACH
def func1(s,t):
    if len(s)!=len(t):
        return False
    counter=[0]*26
    for i in range(len(s)):
        counter[ord(s[i])-ord('a')]+=1
        counter[ord(t[i])-ord('a')]-=1
    
    for i in counter:
        if i!=0:
            return False
    return True