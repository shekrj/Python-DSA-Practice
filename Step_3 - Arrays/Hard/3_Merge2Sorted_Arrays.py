def merge2SortedArrays(arr1, arr2, n, m):
    # Declare 2 pointers:
    left = n - 1
    right = 0

    # Swap elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    # Sort arr1[] and arr2[] individually:
    arr1.sort()
    arr2.sort()