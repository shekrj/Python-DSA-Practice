n=int(input("enter value for n : " ))
for i in range(n):
    for j in range(ord('A'), ord('A')+i+1):
        print(chr(j),end=" ")
    print()

