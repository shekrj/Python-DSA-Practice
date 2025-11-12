def binarySearch(arr, target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        