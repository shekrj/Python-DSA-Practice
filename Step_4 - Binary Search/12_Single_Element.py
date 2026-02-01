def SingleElement(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        # Make sure mid is even
        if mid % 2 == 1:
            mid -= 1  # Ensure mid is even to check pairs

        # Check if the pair is correct
        if arr[mid] == arr[mid + 1]:
            low = mid + 2  # Move to the right half
        else:
            high = mid  # Move to the left half or mid is the answer

    return arr[low]  # low == high at this point