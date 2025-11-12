def longestsubarraywithsumk(arr, k):
    n=len(arr)
    prefixsummap={}
    currentsum=0
    maxlen=0
    for i in range(n):
        currentsum+=arr[i]

        if currentsum==k:
            maxlen=max(maxlen, i+1)
        
        remainingsum=currentsum-k

        if remainingsum in prefixsummap:
            length=i-prefixsummap[remainingsum]
            maxlen=max(maxlen, length)
        
        if currentsum not in prefixsummap:
            prefixsummap[currentsum] = i
    
    return maxlen