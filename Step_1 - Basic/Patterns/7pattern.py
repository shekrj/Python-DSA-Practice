n=int(input("enter value for n "))
for i in range(n):
    # space
    for j in range(n-i-1):
        print(" ", end="")

    # star
    for j in range((i*2+1)):
        print("*",end="")

    # space again
    for j in range(n-i-1):
        print(" ",end="")
    print()
