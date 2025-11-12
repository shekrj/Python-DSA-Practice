from typing import List
import math
class Solution:
    def smallestDivisor(self, arr: List[int], n: int) -> int:
        def totalSum(mid, arr):
            sumi=0
            for i in range(len(arr)):
                sumi+=math.ceil(arr[i]/mid)
            return sumi
        low=1
        high=max(arr)
        res=0
        while low<=high:
            mid=(low+high)//2
            if totalSum(mid, arr)<=n:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res