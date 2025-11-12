def un(arr1, arr2):
    n1=len(arr1)
    n2=len(arr2)
    union=[]
    i=0
    j=0
    while(i<n1 and j<n2):
        if (arr1[i] < arr2[j]):
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
        
    while(i<n1):
        if union[-1] != arr1[i]:
                union.append(arr1[i])
        i+=1
        
    while(j<n2):
        if union[-1] != arr2[j]:
                union.append(arr2[j])
        j+=1


    return union

size1=int(input("Enter size for array 1 : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(size1)]
size2=int(input("Enter size for array 2 : "))
arr2=[int(input(f"Enter element {i+1} : "))for i in range(size2)]
print(un(arr1, arr2))

# def union(arr1, arr2):
#     # Use a set to store unique elements
#     result = set(arr1).union(set(arr2))
#     return list(result)
