from collections import defaultdict

def find_all_subarrays_with_given_sum(arr, k):
    n = len(arr)  # Size of the given array
    pre_sum = 0
    cnt = 0
    mpp = defaultdict(int)

    mpp[0] = 1  # Setting 0 in the map

    for i in range(n):
        # Add current element to prefix sum
        pre_sum += arr[i]

        # Calculate x - k
        remove = pre_sum - k

        # Add the number of subarrays to be removed
        cnt += mpp[remove]

        # Update the count of prefix sum in the map
        mpp[pre_sum] += 1

    return cnt

def subarraySum(nums, k):
    prefix_sum_count = {}  # no base case here
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num

        # Handle subarray from start
        if curr_sum == k:
            count += 1

        # Handle other subarrays
        count += prefix_sum_count.get(curr_sum - k, 0)

        # Update the prefix sum count
        prefix_sum_count[curr_sum] = prefix_sum_count.get(curr_sum, 0) + 1

    return count