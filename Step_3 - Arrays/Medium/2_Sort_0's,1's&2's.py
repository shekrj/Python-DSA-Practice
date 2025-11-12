# DUTCH NATIONAL FLAG ALGORITHM 
def sort0s1s2s(arr):
    n=len(arr)
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
    return arr
n=int(input("Enter size for an array : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(sort0s1s2s(arr1))
        
        


