def MissingNumber(arr):
    n=len(arr)
    sum=(n*(n+1))//2
    s2=0
    for i in range(n):
        s2+=arr[i]
    return sum-s2

n=int(input("Enter size for an arrray : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(MissingNumber(arr1))