n=int(input("Entered Value : "))
l1=[]
for i in range(1, n+1):
    if n%i==0:
        l1.append(i)
print(l1)
# for i in range(1, n + 1):  # Loop from 1 to n
#     l1 = []  # Reinitialize list on every iteration (Incorrect)
#     if n % i == 0:
#         l1.append(i)
#     print(l1)  # This will print the list on each iteration (not what we want)
