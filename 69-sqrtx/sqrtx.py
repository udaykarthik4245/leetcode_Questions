class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        while l<=r:
            mid=(l+r)//2
            squared=mid*mid
            if squared==x:
                return mid
            elif squared<x:
                l=mid+1
            else:
                r=mid-1
        return r
        