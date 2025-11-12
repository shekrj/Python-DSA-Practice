def func(arr):
    hashmap={}
    cnt=0
    totalsum=0
    for i in range(len(arr)):
        if arr[i]==1:
            totalsum+=1
        else:
            totalsum-=1
        if totalsum in hashmap:
            cnt+hashmap[totalsum]
            hashmap[totalsum]+=1
        else:
            totalsum[hashmap] = 1
    return  cnt