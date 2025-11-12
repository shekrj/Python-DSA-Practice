# def fun(i,n):
#     if(i==0):
#         return
    
#     fun(i-1,n)
#     print(i)
    

# n=int(input("Enter value for n : "))
# fun(n,n)
def fun(i,n):
    if(i>n):
        return
    
    fun(i+1,n)
    print(i)
n=int(input("Enter value for n : "))
fun(1,n)