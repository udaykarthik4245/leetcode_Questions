from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        major=n//2

        # nums.sort()
        # count=1
        # for i in range(1,n):
        #     if nums[i]==nums[i-1]:
        #         count+=1
        #         if count>major:
        #             return nums[i]
        #     else:
        #         count=1
        # if n==1:
        #     return nums[0]

        # return -1
        c=Counter(nums)
        for i in c:
            if c[i]>major:
                return i
        return -1

        