class Solution:
    def countPartitions(self, a, maxSum):
        n = len(a)  # size of array
        partitions = 1
        subarraySum = 0
        for i in range(n):
            if subarraySum + a[i] <= maxSum:
                # insert element to current subarray
                subarraySum += a[i]
            else:
                # insert element to next subarray
                partitions += 1
                subarraySum = a[i]
        return partitions

    def splitArray(self, nums, k: int) -> int:

        low = max(nums)
        high = sum(nums)
    # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            partitions = self.countPartitions(nums, mid)
            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
        