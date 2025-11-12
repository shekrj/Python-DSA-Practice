def reverseano(n):
    rev=0
    cnt=0
    ld=0
    while n>0:
        ld=n%10
        cnt+=1 
        rev=rev*10+n%10
        n=n//10
    return cnt, rev

    # if n>0:
    #     m=str(abs(n))[::-1]
    
    # if n<0:
    #     m=str(abs(n))[::-1]
    #     m=int(m)*-1
    # return m

n=5321
print(reverseano(n))