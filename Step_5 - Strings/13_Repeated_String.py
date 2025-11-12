class Solution:
    def func(self, s1: str, s2: str) -> int:
        temp=s1
        if s2 in s1:
            return 1              
        cnt=1
        i=0
        while len(s1)<len(s2)+len(temp):
            s1+=temp
            cnt+=1
            if s2 in s1:
                return cnt
            i+=1
        return -1