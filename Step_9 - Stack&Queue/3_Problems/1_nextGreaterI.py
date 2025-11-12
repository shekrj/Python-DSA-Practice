# Brute Force

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        ans=[]
        for i in range(len(nums1)):
            found=False
            NGE=-1
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    found=True
                if found and nums2[j]>nums1[i]:
                    NGE=nums2[j]
                    break
            ans.append(NGE)
        return ans


# Optimal Approach

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        st=[]
        hashmap={}
        for i in range(len(nums2)-1, -1, -1):
            while st and nums2[i]>=st[-1]:
                st.pop()
            if st:
                hashmap[nums2[i]]=st[-1]
            else:
                hashmap[nums2[i]]=-1
            st.append(nums2[i])
        result=[]
        for i in nums1:
            result.append(hashmap[i])
        return result           