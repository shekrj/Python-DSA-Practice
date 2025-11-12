class Solution:
    def subsetSums(self, arr):
        res = []
        def backtrack(i, path, total):
            if i == len(arr):
                res.append(total)   # since this version asks for sums
                return
            # choice 1: skip arr[i]
            backtrack(i+1, path, total)
            # choice 2: include arr[i]
            backtrack(i+1, path+[arr[i]], total + arr[i])
        backtrack(0, [], 0)
        return res
