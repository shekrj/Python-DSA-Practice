def leader(arr1):
    n=len(arr1)
    temp=[]
    maxi=float('-inf')
    for i in range(n-1, -1, -1):
        if arr1[i]>maxi:
            temp.append(arr1[i])
            maxi=max(maxi, arr1[i])
    return temp

n=int(input("Enter size for an array : "))
arr2=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(leader(arr2))     
