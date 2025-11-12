#IMPORTANT
def longestSubarrayWithSumK(a,k):
    n=len(a)
    left, right= 0, 0
    currentSum=0
    maxLen=0

    while right<n:
        currentSum+=a[right]

        while left<=right and currentSum>k:
            currentSum-=a[left]
            left+=1
        
        if currentSum==k:
            maxLen=max(maxLen, right-left+1)
        
        right+=1

    return maxLen
