class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n=len(arr)
        lsum=0
        rsum=0
        maxsum=0
        rindex=n-1
        for  i in range(k):
            lsum+=arr[i]
            maxsum=lsum
        for i in range(k-1,-1,-1):
            lsum-=arr[i]
            rsum+=arr[rindex]
            rindex-=1
            maxsum=max(maxsum,lsum+rsum)
        return maxsum
        