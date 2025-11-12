# def sumProblem(arr, target):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n):
#             if arr[j] + arr[i] == target and arr[i]!= arr[j]:
#                 return "YES"
#     return "NO"

# n=int(input("Enter size for an array : "))
# target=int(input("Enter target sum : "))
# arr1=[int(input(f"Enter element {i+1} : "))for i in range(n)]
# print(sumProblem(arr1, target)) #BRUTE FORCE

def TwoSumProblem(arr, target):
    n=len(arr)
    hash_map={}
    for i in range(n):
        num=arr[i]
        more_needed=target-num
        if more_needed in hash_map:
            return [hash_map[more_needed], i]
        hash_map[num]=i
    return [-1, -1]        #BETTER APPROACH FOR 1ST VARIANT(RETURN YES OR NO), OPTIMAL APPROACH FOR 2ND VARIANT(RETURN INDICES OF ELEMENTS).

