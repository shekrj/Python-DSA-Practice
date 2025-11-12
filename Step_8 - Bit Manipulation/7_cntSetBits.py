'''

cnt=0
while n!=1:
    if n%2==1:     or  cnt+=n&1      or      while n!=0:
        cnt+=1         n=n>>1                n=n&(n-1)
    n//=2                                    cnt+=1 
cnt+=1
return cnt

'''