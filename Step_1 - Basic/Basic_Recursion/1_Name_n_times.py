def fun(i,n):
    if(i>n):
        return
    print("Harry")
    fun(i+1,n)
n=int(input("Enter value for n : "))
fun(1,n)