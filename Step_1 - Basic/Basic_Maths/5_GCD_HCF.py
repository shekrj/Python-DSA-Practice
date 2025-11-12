a=int(input("Enter 1st number for finding it's GCD/HCF : "))
b=int(input("Enter 2nd number for finding it's GCD/HCF : "))
while(a > 0 and b > 0):
    if a>b:
        a=a%b
    
    else:
        b=b%a
if a==0:
    print(b, " is the GCD/HCF.")
else:
    print(a, " is the GCD/HCF.")

