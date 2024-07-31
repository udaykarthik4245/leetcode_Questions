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
            if zeroes<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return  (maxlen)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l = r = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1


        