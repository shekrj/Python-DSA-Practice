class Solution:
    # Function to count inversions in the array.
    def inversionCount(self, arr):
        def merge(arr, low, mid, high):
            temp = []  # Temporary array
            left = low  # Starting index of left half
            right = mid + 1  # Starting index of right half

            # Modification 1: Count variable to count the pairs
            cnt = 0  

            # Storing elements in temp array in sorted manner
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    cnt += (mid - left + 1)  # Modification 2
                    right += 1

            # If elements in the left half are still left
            while left <= mid:
                temp.append(arr[left])
                left += 1

            # If elements in the right half are still left
            while right <= high:
                temp.append(arr[right])
                right += 1

            # Transferring all elements from temp to arr
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

            return cnt  # Modification 3
        
        def mergeSort(arr, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            inv_count = mergeSort(arr, low, mid)  # Left part inversions
            inv_count += mergeSort(arr, mid + 1, high)  # Right part inversions
            inv_count += merge(arr, low, mid, high)  # Merge step inversions
            return inv_count

        return mergeSort(arr, 0, len(arr) - 1)