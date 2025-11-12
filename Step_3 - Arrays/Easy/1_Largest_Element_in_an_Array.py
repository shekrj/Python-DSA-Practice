# ARRAY - Array is a linear data structure which contains any data type but all the elements should be of same data type.

n=int(input("Enter size of an array : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]

def largest_element(arr):
    n=len(arr)
    largest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
    return largest

print(largest_element(arr1))

