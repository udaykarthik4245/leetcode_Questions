import numpy as np 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l=[]
        # # m=[]

        n=len(nums)
        # for i in range(n):
        #     temp_nums = nums[:i] + nums[i+1:]
        #     product=1
        #     for j in temp_nums:
        #         product*=j
        #     l.append(product)
        # return l
                                 # approach 2
        result = [1] * n

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result
        
        # for i in range(0,len(nums)-1):
        #     nums.remove(i)
        #     product=int(np.prod(nums[:]))
        #     nums.insert(i,nums[i])
        #     l.append(product)
         
        return l
        