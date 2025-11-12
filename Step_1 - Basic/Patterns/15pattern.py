n=int(input("enter value for n : " ))
for i in range(n):
    for j in range(ord('A'), ord('A')+(n-i)):
        print(chr(j),end=" ")
    print()

