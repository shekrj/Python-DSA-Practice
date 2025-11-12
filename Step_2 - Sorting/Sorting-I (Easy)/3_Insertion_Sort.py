# (INSERTION SORT) - Takes an element & places it in its correct order

def in_sort(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1

#     print(f"Array after INSERTION SORT : {arr} ")
    
# n=int(input("Enter size of array : "))
# arr=[int(input(f"Enter Element no. {i+1} : ")) for i in range(n)]
# print(f"Array before INSERTION SORT : {arr} ")
# in_sort(arr)


# TIME COMPLEXITY - O(N^2), FOR BEST CASE - O(N) - linear time complexity if the array is already sorted after optimising the code for counting no. of swap. // Same as Bubble Sort
