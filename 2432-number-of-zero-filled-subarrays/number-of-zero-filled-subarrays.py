class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        prev=0
        total=0
        for i in nums:
            if i==0:
                prev+=1
                total+=prev
            else:
                prev=0
        return total
        