from typing import List
class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        res=[]
        arr.sort()
        def backtrack(start, path, target):
            if target==0:
                res.append(path[:])
            if target<0:
                return
            prev=-1
            for i in range(start, len(arr)):
                if arr[i]==prev:
                    continue
                path.append(arr[i])
                backtrack(i+1, path, target-arr[i])
                path.pop()
                prev=arr[i]
        backtrack(0, [], target)
        return res
