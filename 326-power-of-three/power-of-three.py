class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        maxi=3**20


        return n>0 and  maxi%n==0
        #n^(n-1) ==1
    # recursion approach
        if n == 0:
            return False
        if n%3 == 0:
            return self.isPowerOfThree(n//3)
        if n == 1:
            return True
        else:
            return False
    # brute force approach
        if n <= 0:  
            return False
        while n % 3 == 0:  
            n /= 3
        return n == 1
        if n ==1:
            return True
