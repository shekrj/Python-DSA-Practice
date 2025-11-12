n=int(input("enter value for n : "))
for i in range(n):
    for j in range(ord('E')-i,ord('E')+1):
        print(chr(j), end="")
    print()