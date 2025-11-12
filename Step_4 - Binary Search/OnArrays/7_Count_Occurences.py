def LastOccurence(arr, target):
    n=len(arr)
    low=0
    high=n-1
    result1=-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            result1=mid
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return result1

def FirstOccurence(arr, target):
    n=len(arr)
    low=0
    high=n-1
    result2=-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            result2=mid
            high=mid-1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1   
    return result2

def countOccurrences(arr, target):
    first=FirstOccurence(arr, target)
    last=LastOccurence(arr, target)
    if first==-1:
        return 0
    Total_Occurences=last-first+1
    return Total_Occurences


n = int(input("Enter size of the array: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
target = int(input("Enter the target number: "))

print("Occurrences of", target, ":", countOccurrences(arr, target))
    