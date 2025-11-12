def rightK(arr, k):
    n=len(arr)
    k=k%n
    def reversal(start, end):
        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
        return arr
    reversal(0, n-1)
    reversal(0, k-1)
    reversal(k, n-1)
    return arr

k=int(input("Enter no. of places : "))
arr=list(map(int, input("Enter elements seperated by space : ").split()))
print(rightK(arr, k))