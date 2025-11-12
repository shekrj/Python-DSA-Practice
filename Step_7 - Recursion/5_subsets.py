from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            # choice 1: skip nums[i]
            backtrack(i+1, path)
            # choice 2: include nums[i]
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
        backtrack(0, [])
        return res
