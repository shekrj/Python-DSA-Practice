class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        result = []

        for mask in range(1 << n):  # from 0 to 2^n - 1
            subset = []
            for j in range(n):
                if mask & (1 << j):  # if j-th bit is set
                    subset.append(nums[j])
            result.append(subset)
    
        return result