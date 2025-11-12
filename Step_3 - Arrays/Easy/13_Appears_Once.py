def xor(arr):
    xorr=0
    for i in arr:
        xorr^=i
    return xorr

n=int(input("Enter size for an array : "))
arr=[int(input(f"Enter element {i+1} : "))for i in range(n)]
print(xor(arr))