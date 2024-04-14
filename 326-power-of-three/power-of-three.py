class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        maxi=3**20
        return n>0 and  maxi%n==0#n^(n-1) ==1