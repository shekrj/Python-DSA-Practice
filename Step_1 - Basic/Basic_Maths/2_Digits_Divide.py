n=abs(int(input("Enter the no. : ")))
count=0
for i in str(n):
    digit=int(i)
    if n%digit==0 and digit!=0:
        count+=1
print(count)

