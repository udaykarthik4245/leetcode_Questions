from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        c=Counter(nums)
        for n,count in c.items():
            if count==1:
                return n
        