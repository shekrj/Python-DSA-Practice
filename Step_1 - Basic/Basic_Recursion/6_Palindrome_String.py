def Pal_check(n, start, end):
    if start>=end:
        return True
    if n[start]!=n[end]:
        return False
    return Pal_check(n, start+1, end-1)
n=str(input("Entered String : "))
if Pal_check(n, 0, len(n)-1):
    print("True")
else:
    print("False")
