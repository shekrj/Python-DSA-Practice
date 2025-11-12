# KADANE'S ALGORITHM
def maxSubarray(arr):
    n=len(arr)
    maxsum=float('-inf')
    sum=0
    for i in range(n):
        sum+=arr[i]
        maxsum=max(sum, maxsum)

        if sum<0:
            sum=0
    return maxsum