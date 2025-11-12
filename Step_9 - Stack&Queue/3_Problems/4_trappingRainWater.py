class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
    
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
    
    
from typing import List
class Solution:
    def trap(self, arr: List[int]) -> int:
        leftMax=[0]*len(arr)
        leftMax[0]=arr[0]
        for i in range(1, len(arr)):
            leftMax[i]=max(leftMax[i-1], arr[i])
        rightMax=[0]*len(arr)
        rightMax[-1]=arr[-1]
        for i in range(len(arr)-2, -1, -1):
            rightMax[i]=max(rightMax[i+1], arr[i])
        water=0
        for i in range(len(arr)):
            water+=min(leftMax[i], rightMax[i])-arr[i]
        return water