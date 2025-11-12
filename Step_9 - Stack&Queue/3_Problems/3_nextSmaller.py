class Solution:
    def nextSmallerEl(self, nums1):
        st=[]
        res=[-1]*len(nums1)
        for i in range(len(nums1)-1, -1, -1):
            curr=nums1[i]
            while st and curr<=st[-1]:
                st.pop()
            if st:
                res[i]=st[-1]
            st.append(curr)
        return res