from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    #main optimal solution 
        candidate = None
        count = 0
 
        for num in nums:
            if count == 0:
                candidate = num
            
            count += 1 if candidate == num else -1
        return candidate
    
    #solution using sort and comparing 

            # n=len(nums)
        # major=n//2

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

        # 2nd solution using hashmap
        # c=Counter(nums)
        # for i in c:
        #     if c[i]>major:
        #         return i
        # return -1

        