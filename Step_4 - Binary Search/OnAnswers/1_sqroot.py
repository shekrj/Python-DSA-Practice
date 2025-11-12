def sqroot(n):
    low=1
    high=n
    temp=0
    while low<=high:
        mid=(low+(high-low))//2
        if (mid*mid)<=n:
            temp=mid
            low=mid+1
        else:
            high=mid-1
    return temp
