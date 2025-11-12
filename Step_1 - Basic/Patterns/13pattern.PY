n=int(input("enter value for n : "))
num=1
for i in range(1,n):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()