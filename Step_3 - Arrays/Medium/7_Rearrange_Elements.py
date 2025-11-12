# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         temp=[0]*n
#         posIndex=0
#         negIndex=1
#         for i in range(n):
#             if nums[i]>0:
#                 temp[posIndex]=nums[i]
#                 posIndex+=2
#             else:
#                 temp[negIndex]=nums[i]
#                 negIndex+=2
#         return temp    
# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         pos_arr = [num for num in nums if num >= 0]  # Extract positive numbers
#         neg_arr = [num for num in nums if num < 0]   # Extract negative numbers
    
#         result = []
#         for i in range(n // 2):
#             result.append(pos_arr[i])  # Append positive number
#             result.append(neg_arr[i])  # Append negative number
    
#         return result

# 2ND VARIANT -