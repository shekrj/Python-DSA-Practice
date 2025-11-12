class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        stack = []
        ple = [-1] * n  # Previous Less Element indices
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                ple[i] = stack[-1]
            stack.append(i)

        stack = []
        nle = [n] * n  # Next Less Element indices
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
            res %= MOD

        return res