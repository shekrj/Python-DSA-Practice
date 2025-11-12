class Solution:
    def largestRectangleArea(self, heights):
        n=len(heights)

        def prevSmallerEl(heights):
            st=[]
            
            left=[-1]*n
            for i in range(len(heights)):
                while st and heights[i]<=heights[st[-1]]:
                    st.pop()
                if st:
                    left[i]=st[-1]
                st.append(i)
            return left

        def nextSmallerEl(heights):
            st=[]
            right=[n]*n
            for i in range(len(heights)-1, -1 ,-1):
                while st and heights[i]<=heights[st[-1]]:
                    st.pop()
                if st:
                    right[i]=st[-1]
                st.append(i)
            return right
        
        maxArea=0
        left=prevSmallerEl(heights)
        right=nextSmallerEl(heights)
        for i in range(n):
            width=right[i]-left[i]-1
            area=heights[i]*width
            maxArea=max(maxArea, area)
        return maxArea