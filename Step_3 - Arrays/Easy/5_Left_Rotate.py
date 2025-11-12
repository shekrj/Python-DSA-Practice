# def leftRotate(arr):
#     n=len(arr)
#     for i in range(n-1):
#         arr[i+1], arr[i] = arr[i], arr[i+1]

#     return arr



# n=int(input("Enter size for an array : "))
# arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
# print(leftRotate(arr1))

def leftRotate(arr):
    n=len(arr)
    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr
n=int(input("Enter size for an array : "))
arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(leftRotate(arr1))



