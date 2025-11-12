def max_product_subarray(arr):
    n = len(arr)  # Size of array

    pre, suff = 1, 1
    ans = float('-inf')

    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= arr[i]
        suff *= arr[n - i - 1]
        ans = max(ans, pre, suff)

    return ans

# Example usage:
arr = [2, 3, -2, 4]
print(max_product_subarray(arr))  # Output: 6