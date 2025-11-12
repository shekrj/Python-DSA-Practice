def func(n):
    s="1"
    for _ in range(n):
        result=""
        cnt=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                cnt+=1
            else:
                temp+=str(cnt)+s[i]
                cnt=0
        temp+=str(cnt)+s[-1]
        s=temp
