# MOORE'S VOTING ALGORITHM
def majorityElement(arr):
    n=len(arr)
    el=None
    cnt=0
    for i in range(n):
        if cnt==0:
            el=arr[i]
            cnt=1
        elif el==arr[i]:
            cnt+=1
        else:
            cnt-=1
    
    cnt1=0
    for i in range(n):
        if arr[i] == el:
            cnt1+=1
    if cnt1>(n/2):
        return el
    return -1
