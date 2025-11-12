## n=int(input("Your input : "))
## print(len(str(abs(n))))
# n=abs(int(input("Your input : ")))
# count=0
# for i in str(n):
#     count+=1
# print(count)
import math
n=int(input("enter value : "))
count=int(math.log10(n)+1)
print(count)