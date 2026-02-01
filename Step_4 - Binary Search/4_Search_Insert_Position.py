from typing import List
class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        low=0
        high=len(arr)-1
        possibleSol=len(arr)
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                possibleSol=mid+1
                low=mid+1
            else:
                possibleSol=mid
                high=mid-1
        return possibleSol            