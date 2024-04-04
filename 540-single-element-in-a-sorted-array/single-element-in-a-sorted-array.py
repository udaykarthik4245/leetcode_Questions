from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        low=1
        high=n-2
        if(n==1) :
            return nums[0]
        if(nums[0]!=nums[1]) :
            return nums[0]
        if(nums[n-1]!=nums[n-2]):
             return nums[n-1]
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                low=mid+1
            else:
                high=mid-1
        return -1
#easily readeable solution 
        # we can tell by parity
        # even and following odd index should be the same
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # odd
            if mid % 2:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]
        

#o(n) complexity using dictionary counters
        c=Counter(nums)
        for n,count in c.items():
            if count==1:
                return n
        