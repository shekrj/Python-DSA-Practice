# n=int(input("entered value: "))
# sum=0
# for i in range(1, n+1):
#     sum+=i
# print(sum)
def sum(n):
    if (n==0):
        return 0
    return n+sum(n-1)

n=int(input("Entered Value : "))
print(sum(n))
