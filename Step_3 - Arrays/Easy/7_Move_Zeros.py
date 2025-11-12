def moveZeros(arr):
    n=len(arr)
    count=0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count +=1
    for i in range(count, n):
        arr[i] = 0
       
    return arr
n=int(input("Enter size for an array : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(moveZeros(arr1))
