def selSort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min=j
        arr[min], arr[i]=arr[i], arr[min]

def bubSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def inSort(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
