class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        l1=(n&n-1)==0
        l2=(n&0xaaaaaaaa)==0
        return l1 & l2
        