# n=int(input("Enter the no. : "))
# l1=list(str(n))
# l1.reverse()
# l2=(int("".join(l1)))
# if (l2==n):
#     print("Palindrome No.")
n=int(input("Enter the no. : "))
if str(n)==str(n)[::-1]:
    print("Palindrome")
else:
    print("Nope")