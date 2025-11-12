class solution:
    def canWePlaceCows(self, arr, dist, cows):
        cntCows=1
        lastCow=arr[0]
        for i in range(len(arr)):
            if arr[i]-lastCow>=dist:
                cntCows+=1
                lastCow=arr[i]
            if cntCows>=cows:
                return True
        return False
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n=len(stalls)
        low=0
        high=stalls[n-1]-stalls[0]
        while low<=high:
            mid=(low+high)//2 
            if self.canWePlaceCows(stalls, mid, k):
                low=mid+1
            else:
                high=mid-1
        return high


            