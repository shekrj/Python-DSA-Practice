from typing import List
class Solution:
    def func(self, arr: List[int], k: int) -> int:
        hashmap={}
        presum=0
        length=0
        maxLen=0
        for i in range(len(arr)):
            presum+=arr[i]
            if presum==k:
                length=i+1
                maxLen=max(length, maxLen)
            remainingSum=presum-k
            if remainingSum in hashmap:
                length=i-hashmap[remainingSum]
                maxLen=max(length, maxLen)
            if presum not in hashmap:
                hashmap[presum]=i
        return maxLen
    

    def func2(self, arr: List[int], k: int) -> int:
        hashmap={}
        cnt=0
        total=0
        hashmap[0]=1
        for i in range(len(arr)):
            total+=arr[i]
            removed=total-k
            if hashmap[removed]:
                cnt+=hashmap[removed]
            if total not in hashmap:
                hashmap[total]=1
            else:
                hashmap[total]+=1
        return cnt


    def func3(self, arr: List[int], k: int) -> int:
        hashmap={}
        for i in range(len(arr)):
            complement=k-arr[i]
            if complement in hashmap:
                return hashmap[complement], i
            if arr[i] not in hashmap:
                hashmap[arr[i]]=i
        return -1, -1
    

    def func4(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        row=[0]*n
        col=[0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(n):
            for j in range(m):
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0        
                    
    
    def func5(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()