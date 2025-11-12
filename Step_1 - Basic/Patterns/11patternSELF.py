n=int(input("Enter value for n : "))
for i in range(n):
    start =  1 if i%2==0 else 0
    for j in range(i+1):
        print(start, end="")
        start=1-start
    print()