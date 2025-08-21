class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        res=-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                res=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return res
