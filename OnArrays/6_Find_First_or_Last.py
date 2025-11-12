def Last(arr, target):
    n=len(arr)
    low=0
    high=n-1
    result=-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            result=mid
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return result
