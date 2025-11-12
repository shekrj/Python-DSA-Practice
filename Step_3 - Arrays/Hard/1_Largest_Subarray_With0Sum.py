def max_len(arr):
    mpp = {}  # Dictionary to store prefix sum
    maxi = 0
    total_sum = 0

    for i in range(len(arr)):
        total_sum += arr[i]

        if total_sum == 0:
            maxi = i + 1
        elif total_sum in mpp:
            maxi = max(maxi, i - mpp[total_sum])
        else:
            mpp[total_sum] = i  # Store first occurrence

    return maxi

# Example
arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(max_len(arr))  # Output: 5