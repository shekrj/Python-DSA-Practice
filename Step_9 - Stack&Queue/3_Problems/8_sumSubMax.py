class Solution:
    def subSubarrayMaximum(self, nums):
        mod=10**9+7
        n=len(nums)

        st=[]
        pge=[-1]*n
        for i in range(n):
            while st and nums[i]>nums[st[-1]]:
                st.pop()
            if st:
                pge[i]=st[-1]
            st.append(i)
        
        st=[]
        nge=[n]*n
        for i in range(n-1, -1, -1):
            while st and nums[i]>=nums[st[-1]]:
                st.pop()
            if st:
                nge[i]=st[-1]
            st.append(i)
        res=0
        for i in range(n):
            left=i-pge[i]
            right=nge[i]-i
            res+=nums[i]*left*right
        return res%mod