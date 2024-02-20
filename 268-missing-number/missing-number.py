class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nsum= n*(n+1)//2
        val=nsum-sum(nums)
        # res=[]
        return val 
        