class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first=0
        for i in nums:
            if i!=0:
                nums[first]=i
                first+=1
        for i in range(first,len(nums)):
            nums[i]=0
        return nums