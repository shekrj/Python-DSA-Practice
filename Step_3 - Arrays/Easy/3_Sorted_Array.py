def isSorted(arr):
    n=len(arr)
    for i in range(1, n):
        if arr[i]<arr[i-1]:
            return False
    return True

n=int(input("Enter size for an array : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(arr1)
print(isSorted(arr1))

