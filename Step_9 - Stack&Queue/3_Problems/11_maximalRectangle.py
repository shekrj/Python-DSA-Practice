class Solution:
    def largestRectangle(self, heights):
        n = len(heights)

        def prevSmallerEl(heights):
            st = []
            left = [-1] * n
            for i in range(n):
                while st and heights[i] <= heights[st[-1]]:
                    st.pop()
                if st:
                    left[i] = st[-1]
                st.append(i)
            return left

        def nextSmallerEl(heights):
            st = []
            right = [n] * n
            for i in range(n - 1, -1, -1):
                while st and heights[i] <= heights[st[-1]]:
                    st.pop()
                if st:
                    right[i] = st[-1]
                st.append(i)
            return right

        left = prevSmallerEl(heights)
        right = nextSmallerEl(heights)

        maxArea = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            maxArea = max(maxArea, area)

        return maxArea

    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        maxArea = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea, self.largestRectangle(heights))

        return maxArea
