class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        maxlen=0
        n=len(arr)
        zeroes=0
        l,r=0,0
        while r<n:
            # zeroes=0
            if arr[r]==0:
                zeroes+=1
            if zeroes>k:
                if arr[l]==0:
                    zeroes-=1
                l+=1
            r+=1
            maxlen=max(maxlen,r-l)
        return  (maxlen)
        