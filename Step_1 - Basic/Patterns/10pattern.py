n=int(input("Enter value for n : "))
for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print()
for i in range(1, n):
    for j in range(n-i):
        print("*", end="")
    print()
# n = int(input("Enter value for n: "))

# # Top half of the pyramid (including the middle row)
# for i in range(1, n + 1):
#     print("*" * i)

# # Bottom half of the pyramid (excluding the middle row)
# for i in range(1, n):
#     print("*" * (n - i))
