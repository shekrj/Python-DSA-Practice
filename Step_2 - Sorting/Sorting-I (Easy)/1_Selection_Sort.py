# (SELECTION SORT) - Selects minimum & swaps

def sel_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1, n):
            if arr[j]<arr[min]:
                min=j
        arr[min], arr[i]=arr[i], arr[min]

#     print("Array after Selection Sort : ")
#     # print(*arr, sep=" ")
#     print(arr)

# n=int(input("Enter value for n : "))
# arr=[int(input(f"Enter element {i+1} : ")) for i in range(n)]
# print(f"Array before Selection Sort : {arr}")
# sel_sort(arr)

# TIME COMPLEXITY - O(N^2) - For ALL CASES **
