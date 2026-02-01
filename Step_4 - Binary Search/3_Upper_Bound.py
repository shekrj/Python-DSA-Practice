def UpperBound(arr, target):
    n=len(arr)
    low=0
    high=n-1
    i=n
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]<=target:
            low=mid+1
        else:
            i=mid
            high=mid-1
    return i