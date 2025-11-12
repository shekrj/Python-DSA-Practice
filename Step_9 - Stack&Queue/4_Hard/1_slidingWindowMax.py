# Brute Force

class Solution:
    def maxSlidingWindow(self, nums, k):
        res=[]
        for i in range(len(nums)-k+1):
            maxi=nums[i]
            for j in range(i, i+k):
                maxi=max(nums[j], maxi)
            res.append(maxi)
        return res

# Optimal

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k:int) -> List[int]:
        from collections import deque
        n=len(nums)
        if not nums or k==0:
            return []
        dq=deque()
        res=[]
        for i in range(n):
            if dq and dq[0]<=i-k:
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
        return res