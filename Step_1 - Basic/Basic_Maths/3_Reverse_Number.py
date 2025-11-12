# n=int(input("Enter the no. you want to reverse : "))
# l1=list(str(n))
# l1.reverse()
# print(int(("".join((l1)))))

# n=int(input("enter value : "))
# l1=str(n)[::-1]
# print(int(l1))
                            

n = int(input("Enter an integer: "))
revNum = 0
while n > 0:
    lastdigit = n % 10
    revNum = (revNum * 10) + lastdigit
    n = n // 10
print(revNum)