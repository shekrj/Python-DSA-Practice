def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Merge the two halves into temp
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Add remaining elements from the left half
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Add remaining elements from the right half
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy sorted elements back into the original array
    arr[low:high + 1] = temp


def mergeSort(arr, low, high):
    print(f"mergeSort called with low={low}, high={high}")  # Debugging print
    # Base condition
    if low >= high:
        return

    mid = (low + high) // 2
    print(f"Midpoint: {mid}")  # Debugging print

    # Recursively sort both halves
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)

    # Merge the sorted halves
    merge(arr, low, mid, high)


# Input and function call
n = int(input("Enter size for an array: "))
if n == 0:
    print("Empty array!")
    exit()

arr = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]

mergeSort(arr, 0, n - 1)  # Use n-1 as the last index
print("Sorted array:", arr)
