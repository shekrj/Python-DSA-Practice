class Solution:
    def subArrayRanges(self, nums):
        def sumSubarrayMins(arr):
            n = len(arr)
            stack = []
            ple = [-1] * n
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                if stack:
                    ple[i] = stack[-1]
                stack.append(i)

            stack = []
            nle = [n] * n
            for i in range(n-1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    nle[i] = stack[-1]
                stack.append(i)

            res = 0
            for i in range(n):
                left = i - ple[i]
                right = nle[i] - i
                res += arr[i] * left * right
            return res

        def sumSubarrayMax(arr):
            n = len(arr)
            stack = []
            pge = [-1] * n
            for i in range(n):
                while stack and arr[stack[-1]] <= arr[i]:
                    stack.pop()
                if stack:
                    pge[i] = stack[-1]
                stack.append(i)

            stack = []
            nge = [n] * n
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] < arr[i]:
                    stack.pop()
                if stack:
                    nge[i] = stack[-1]
                stack.append(i)

            res = 0
            for i in range(n):
                left = i - pge[i]
                right = nge[i] - i
                res += arr[i] * left * right
            return res

        return sumSubarrayMax(nums) - sumSubarrayMins(nums)
