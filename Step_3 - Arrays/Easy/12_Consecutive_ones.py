def ConsecutiveOnes(arr):
    n=len(arr)
    count=0
    maxi=0
    for i in range(n):
        if arr[i]==1:
            count+=1
            maxi=max(maxi, count)
        else:
            count=0
    return maxi

n=int(input("Enter size for an arrray : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(ConsecutiveOnes(arr1))