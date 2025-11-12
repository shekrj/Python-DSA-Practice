from typing import List
class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(start, path, target):
            if target==0:
                res.append(path[:])
            if target<0:
                return
            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i, path, target-arr[i])
                path.pop()
        backtrack(0, [], target)
        return res