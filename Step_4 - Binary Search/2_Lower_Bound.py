def LowerBound3condition(arr, target):
    n=len(arr)
    low=0
    high=n-1
    i=n
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            i=mid
            high=mid-1
        elif target>arr[mid]:
            low=mid+1
        else:
            high=mid-1
            i=mid
    return i

def LowerBound2condition(arr, target):
    n=len(arr)
    low=0
    high=n-1
    i=n
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]>=target:
            i=mid
            high=mid-1
        else:
            low=mid+1
    return i
