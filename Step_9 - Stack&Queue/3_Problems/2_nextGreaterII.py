# Brute Force

class Solution:
    def nextGreaterElements(self, nums):
        temp=[]
        for i in range(len(nums)):
            NGE=-1
            found=False
            for j in range(i+1, len(nums)):
                if nums[j]>nums[i]:
                    NGE=nums[j]
                    found=True
                    break
            if not found:
                for j in range(0, i):
                    if nums[j]>nums[i]:
                        NGE=nums[j]    
                        break
            temp.append(NGE)
        return temp



# Optimal

class Solution:
    def nextGreaterElements(self, nums):
        st=[]
        res=[-1]*len(nums)
        for i in range(2*len(nums)-1, -1, -1):
            curr=nums[i%len(nums)]
            while st and curr>=st[-1]:
                st.pop()
            if i<len(nums):
                if st:
                    res[i]=st[-1]
            st.append(curr)
        return res