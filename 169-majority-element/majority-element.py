# from collections import Counter
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
    