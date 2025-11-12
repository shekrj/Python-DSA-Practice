from typing import List
class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[len(arr)-1]>arr[len(arr)-2]:
            return len(arr)-1
        low=1
        high=len(arr)-2
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>=arr[low]<=arr[high]:
                low=mid+1
            else:
                high=mid-1
        return -1