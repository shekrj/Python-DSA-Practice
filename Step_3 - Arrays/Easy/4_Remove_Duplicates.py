def removeDuplicates(arr):
    i=0
    n=len(arr)
    for j in range(n):
        if arr[j]!= arr[i]:
            arr[i+1]=arr[j]
            i+=1
    return i+1

n=int(input("Size of array : "))
arr=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(removeDuplicates(arr))