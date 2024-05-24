class Solution:
    @cache
    def climbStairs(self, n: int) -> int:

            # O(n) with O(1) space complexity

        if n==1: return 1
        if n==2: return 2
        # tb=1
        # ob=2
        # for i in range(n-2):
        #     corr=tb+ob
        #     tb=ob
        #     ob=corr
        # return corr
        # o(2^n)
        two=self.climbStairs(n-2)
        one=self.climbStairs(n-1)
        return one+two