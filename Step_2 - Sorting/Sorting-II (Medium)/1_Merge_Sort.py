# (MERGE SORT) - Divide & Merge

def merge(arr, low , mid, high):
    left=low
    right=mid+1
    temp=[]

    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while left<=mid:
            temp.append(arr[left])
            left+=1

    while right<=high:
            temp.append(arr[right])
            right+=1
    
    for i in range(low, high+1):
        arr[i]=temp[i-low]

def merge_sort(arr, low, high):  #pseudocode
    if low>=high:
        return
    mid=(low+high)//2
    merge_sort(arr, low, mid)       #left-half
    merge_sort(arr, mid+1, high)    #right-half
    merge(arr, low, mid, high)      #merge sorted half

n=int(input("Size of array : "))
arr=[int(input(f"Enter element {i+1} : ")) for i in range(n)]

print("Array before Merge Sort : ", arr)
merge_sort(arr, 0, n-1)
print("Array after Merge Sort : ", arr)

# TIME COMPLEXITY - O(n log n), SPACE COMPLEXITY - O(1) *uses a temp array
