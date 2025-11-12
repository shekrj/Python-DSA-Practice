# (BUBBLE SORT) - Pushes the maximum to the last by adjacent swaps

def bubSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#     print("Array after Bubble Sort : ")
#     print(arr)

# n=int(input("Enter value for n : "))
# arr=[int(input(f"Enter element {i+1} : ")) for i in range(n)]
# print(f"Array before Bubble Sort : {arr}")
# bubble_sort(arr)


# TIME COMPLEXITY - O(N^2), FOR BEST CASE - O(N) - linear time complexity if the array is already sorted after optimising the code for counting no. of swap. // Same as Insertion Sort
           