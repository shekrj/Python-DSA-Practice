class Solution(object):
    def search(self, arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            # Handle duplicates
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
            elif arr[low] <= arr[mid]:  # Left is sorted
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # Right is sorted
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False