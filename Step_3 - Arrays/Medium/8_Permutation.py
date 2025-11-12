class Solution(object):
    def nextPermutation(self, arr):
        breakIndex = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                breakIndex = i
                break

    # If no break point found, reverse the entire array
        if breakIndex == -1:
            return arr.reverse()
            

    # Step 2: Find the next greater element from the end
        for i in range(len(arr) - 1, breakIndex, -1):
            if arr[i] > arr[breakIndex]:
                arr[breakIndex], arr[i] = arr[i], arr[breakIndex]
                break

    # Step 3: Reverse the part after breakIndex
        start = breakIndex + 1
        end = len(arr) - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
