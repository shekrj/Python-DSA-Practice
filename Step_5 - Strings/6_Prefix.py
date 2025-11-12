# BEST APPROACH
class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        res=""
        arr.sort()
        for i in range(len(arr[0])):
            if arr[0][i]==arr[len(arr)-1][i]:
                res+=arr[0][i]
            else:
                break
        return res

# BINARY SEARCH APPROACH
def commonprefix(l1, mid):
    prefix=l1[0][:mid]
    for i in l1:
        if not i.startswith(prefix):
            return False
    return True

def func1(l1):
    if len(l1)==0:
        return ""
    
    lengths=[]
    for i in l1:
        lengths.append(len(i))
    minLen=min(lengths)

    low=0
    high=minLen
    while low<=high:
        mid=(low+high)//2
        if commonprefix(l1, mid):
            low=mid+1
        else:
            high=mid-1

    return l1[0][:low-1]


# COMPACT BINARY SEARCH -
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        minLen = min(len(word) for word in strs)
        low, high = 0, minLen

        def commonprefix(mid):
            prefix = strs[0][:mid]
            return all(word.startswith(prefix) for word in strs)

        while low <= high:
            mid = (low + high) // 2
            if commonprefix(mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:low - 1]       
     