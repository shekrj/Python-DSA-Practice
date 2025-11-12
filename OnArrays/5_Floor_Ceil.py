def floorFunc(arr, target):
    n=len(arr)
    low=0
    high=n-1
    floor=-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            floor=arr[mid]
            return floor

        elif arr[mid]<target:
            floor=arr[mid]
            low=mid+1
        
        else:
            high=mid-1
            
    return floor

