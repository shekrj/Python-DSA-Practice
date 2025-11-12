def kthMissingPostitiveNumber(arr, k):
    n=len(arr)
    for i in range(n):
        if arr[i]<=k:
            k+=1
        else:
            break
    return k