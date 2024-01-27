class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                duplicates += 1
            else:
                nums[i - duplicates] = nums[i]

        return len(nums) - duplicates
        # 2nd approch using while loop
        # i=0
        # while i<len(nums):
        #     if len(nums)==1:
        #         return len(nums)
        #     if nums[i]==nums[i-1]:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)

