class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        neg=n<0
        n=abs(n)
        while n:
            if n%2==1:
                ans*=x
                n=n-1
            else:
                n//=2
                x*=x
        if neg:
            return 1/ans
        return ans