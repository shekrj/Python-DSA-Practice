def linearSearch(arr, k):
    n=len(arr)
    for i in range(n):
        if arr[i] == k:
            return i
    return -1

n=int(input("Enter size for an array : "))
k=int(input("Enter element for linear search : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(linearSearch(arr1, k))