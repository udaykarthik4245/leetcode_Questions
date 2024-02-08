class Solution:
    def numSquares(self, n: int) -> int:
 
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n + 1):
            min_squares = float('inf')
            j = 1
            while j * j <= i:
                remaining = i - j * j
                min_squares = min(min_squares, dp[remaining])
                j += 1
            dp[i] = min_squares + 1
        
        return dp[n]
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        steps = [0 for _ in range(n+1)]
        steps[1] = 1
        
        for i in range(2,n+1):
            j = 1
            nums = []
            while j**2 <= i:
                nums.append(i - j**2)
                j += 1
            steps[i] = min([steps[num]+1 for num in nums])
        return steps[-1]
