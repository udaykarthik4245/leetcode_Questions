class Solution:
    def findDelayedArrivalTime(self, a: int, d: int) -> int:
        if a+d>24:
            return abs(24-(a+d))
        if a+d==24:
            return 0
        else:
            return a+d
        