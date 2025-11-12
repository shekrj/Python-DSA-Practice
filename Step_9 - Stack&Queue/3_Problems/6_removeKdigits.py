# def removeKdigits(s: str, k: int) -> str:
#     res = ""
#     for i in s:
#         while res and k > 0 and res[-1] > i:
#             res = res[:-1]
#             k -= 1
#         res += i
#     res = res[:-k] if k else res
#     return res.lstrip("0") or "0"

class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        st=[]
        for i in s:
            while st and i<st[-1] and k>0:
                st.pop()
                k-=1
            st.append(i)
        while k and st:
            st.pop()
            k-=1
        res=''.join(st).lstrip('0')
        return res if res else '0'
