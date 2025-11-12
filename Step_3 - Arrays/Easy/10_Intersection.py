from typing import List
class Solution:
    def func(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        i=0
        j=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]==arr2[j]:
                if not res or res[-1]!=arr1[i]:
                    res.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i]<arr2[j]:
                i+=1
            else:
                j+=1
        return res