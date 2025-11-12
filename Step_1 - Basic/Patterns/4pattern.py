n=int(input("Enter value for n "))
for row in range(1, n+1):
    for column in range(1, row+1):
        print(row, end=" ")
    print()