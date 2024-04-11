class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        l=b[2:]
        return l.count('1')
        