# BINARY SEARCH ALWAYS ON SORTED SEARCH SPACE

def binarySearch(arr, target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1                                           # ITERATIVE APPROACH

def binarySearch(arr, low, high, target):
    if low>high:
        return -1
    mid=low+(high-low)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binarySearch(arr, mid+1, high, target)
    else:
        return binarySearch(arr, low, mid-1, target)   # RECURSIVE APPROACH
    
# Time Complexity - O(log2(N))