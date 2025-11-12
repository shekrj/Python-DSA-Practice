n=int(input("enter value for n "))
for i in range(n):
    # space
    for j in range(i):
        print(" ", end="")

    # star
    for j in range((n*2)-(i*2)-1):
        print("*",end="")

    # space again
    for j in range(i):
        print(" ",end="")
    print()
