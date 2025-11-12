from typing import List
from collections import deque

class Solution:
    def largestElement(self, arr):
        if not arr:
            return None
        largest=float('-inf')
        for i in range(len(arr)):
            if arr[i]>largest:
                largest=arr[i]
        return largest

    def secondLargest(self, arr):
        if not arr:
            return None
        if len(arr)<2:
            return [arr[0], -1]
        secondLargest=float('-inf')
        largest=float('-inf')
        for i in range(len(arr)):
            if arr[i]>largest:
                secondLargest=largest
                largest=arr[i]
            elif arr[i]>secondLargest and arr[i]<largest:
                secondLargest=arr[i]
        if secondLargest==float('-inf'):
            secondLargest=-1
        return [largest, secondLargest]
    
    def sortedArray(self, arr):
        if not arr:
            return None
        for i in range(len(arr)-1):
            if arr[i+1]<arr[i]:
                return "Not Sorted"
        return "Sorted"
    
    def removeDuplicates(self, arr):
        if not arr:
            return None
        j=0
        for i in range(1, len(arr)):
            if arr[i]!=arr[j]:
                arr[j+1]=arr[i]
                j+=1
        return j+1

    def leftRotateBy1Place(self, arr):
        if not arr:
            return None
        if len(arr)<2:
            return arr
        temp=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[len(arr)-1]=temp
        return arr
    
    def rightRotateBy1Place(self, arr):
        if not arr:
            return None
        if len(arr)<2:
            return arr
        temp=arr[len(arr)-1]
        for i in range(len(arr)-1, 0, -1):
            arr[i]=arr[i-1]
        arr[0]=temp
        return arr
    
    def leftRotateByKPlaces(self, arr: List[int], k: int) -> List[int]:
        if not arr or k==0:
            return arr
        n=len(arr)
        k=k%n
        
        def reversal(start, end):
            while start<=end:
                arr[start], arr[end]=arr[end], arr[start]
                start+=1
                end-=1
            return

        reversal(0, k-1)
        reversal(k, n-1)
        reversal(0, n-1)
        return arr
    
    def rightRotateByKPlaces(self, arr: List[int], k: int) -> List[int]:
        if not arr or k==0:
            return arr
        n=len(arr)
        k=k%n

        def reversal(start, end):
            while start<=end:
                arr[start], arr[end]=arr[end], arr[start]
                start+=1
                end-=1
            return 
        
        reversal(0, n-1)
        reversal(0, k-1)
        reversal(k, n-1)
        return arr
    
    def moveZeros(self, arr: List[int]) -> List[int]:
        if not arr:
            return None
        j=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[j], arr[i]=arr[i], arr[j]
                j+=1
        return arr
    
    def linearSearch(self, arr: List[int], target: int) -> int:
        if not arr:
            return None
        for i in range(len(arr)):
            if arr[i]==target:
                return i
        return -1
    
    def union(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s1=set()
        for i in arr1:
            s1.add(i)
        for i in arr2:
            s1.add(i)
        return sorted(s1)
    
    def intersection(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not arr1 or not arr2:
            return None
        n=len(arr1)
        m=len(arr2)
        i=0
        j=0
        res=[]
        while i<n and j<m:
            if arr1[i]<arr2[j]:
                i+=1
                continue
            elif arr1[i]>arr2[j]:
                j+=1
                continue
            else:
                if not res or res[-1]!=arr1[i]:
                    res.append(arr1[i])
                i+=1
                j+=1
        return res
    
    def missingNoLEETCODE(self, arr: List[int]) -> int:
        n=len(arr)
        expectedSum=n*(n-1)//2
        preSum=0
        for i in arr:
            preSum+=i
        return expectedSum-preSum
    
    def missingNoGFG(self, arr: List[int]) -> int:
        n=len(arr)+1
        expectedSum=n*(n-1)//2
        preSum=0
        for i in arr:
            preSum+=i
        return expectedSum-preSum
    
    def maxConsecutiveOnes(self, arr: List[int]) -> int:
        cnt=0
        maxCnt=0
        for i in range(len(arr)):
            if arr[i]==1:
                cnt+=1
                maxCnt=max(cnt, maxCnt)
            else:
                cnt=0
        return maxCnt
    
    def appearsOnce(self, arr: List[int]) -> int:
        