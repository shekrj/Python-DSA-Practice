# (QUICK SORT) - Divide & Conquer - 1. Pick a pivot & place it in its correct place.
#                                   2. Smaller on the left and larger on the right.
def partition(arr, low, high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low , high):
    if low<high:
        p_index=partition(arr, low, high)
        quick_sort(arr, low, p_index-1)
        quick_sort(arr, p_index+1, high)

arr = [4, 6, 2, 5, 7, 9, 1, 3]
print("Array before Quick Sort:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Array after Quick Sort:", arr)



























# TIME COMPLEXITY - O(n log n) // Same as MERGE SORT, SPACE COMPLEXITY - O(1) *does not uses a temp array like in Merge Sort
