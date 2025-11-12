import math
class Solution:        
    def largest(self, arr):
        n=len(arr)
        maxi=float('-inf')
        for i in range(n):
            if arr[i]>maxi:
                maxi=arr[i]
        return maxi
    def calculate_totalhours(self, arr, hourly):
        total_hours=0
        n=len(arr)
        for i in range(n):
            total_hours+=math.ceil(arr[i]/hourly)
        return total_hours
    def minEatingSpeed(self, piles, h):
        low=1
        high=self.largest(piles)
        while low<=high:
            mid=(low+high)//2
            total_hours=self.calculate_totalhours(piles, mid)
            if total_hours<=h:
                high=mid-1
            else:
                low=mid+1
        return low