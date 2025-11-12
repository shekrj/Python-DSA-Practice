def func(a,b,n):
    x=a
    y=b
    while y!=0:
        x, y = y, x% y
    gcd=x
    lcm=(a*b)//gcd
    return (n//lcm)+1