class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        closest=float('-inf')
        # float('-inf')
        for num in nums :
            # if closest is None:
            #     closest=num
            
                if abs(num)<abs(closest):
                    closest=num
                elif abs(num)==abs(closest):
                    closest=max(closest,num)
        return closest


