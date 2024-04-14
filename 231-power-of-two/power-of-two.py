class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n==0:
            return False
        else:
            return n & (n-1)==0
        

        return n>0 and log(n,2)%1==0
        # brute force approach
        i = 0
        while 2**i <= n:
            if 2**i == n:
                return True
            else:
                i += 1
        return False 
        # using xor and operation
        return n != 0 and n == (n^(n-1)) & n
