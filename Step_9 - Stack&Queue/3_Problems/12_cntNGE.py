# BRUTE - FORCE SOLUTION ->
class Solution:
    def cntNGEs(self, nums):
        n=len(nums)
        NGE=[0]*n
        for i in range(n):
            cnt=0
            for j in range(i+1, n):
                if nums[j]>nums[i]:
                    cnt+=1
            NGE[i]=cnt
        return NGE
