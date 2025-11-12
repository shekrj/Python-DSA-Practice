# KADANE'S ALGORITHM
def maxSubarray(arr):
    n=len(arr)
    maxsum=float('-inf')
    tempsum=0
    ansStart=-1
    ansEnd=-1
    for i in range(n):
        if tempsum==0:
            start=i
        if tempsum>maxsum:
            maxsum=tempsum
            ansStart=start, ansEnd=i

        if tempsum<0:
            tempsum=0

    return maxsum