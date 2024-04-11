class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        major=n//2
        nums.sort()
        count=1
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                count+=1
                if count>major:
                    return nums[i]
            else:
                count=1
        for i in nums:
            if n==1:
                return i

        return -1

        