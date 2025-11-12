def maxProfit(arr):
    n=len(arr)
    maxPro=0
    minPrice=float('inf')
    for i in range(n):
        minPrice=min(minPrice, arr[i])
        maxPro=max(maxPro, arr[i]-minPrice)
    return maxPro 