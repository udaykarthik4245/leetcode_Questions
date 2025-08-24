class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=list(s)
        lt=list(t)
        iterator=iter(t)
        ans=all(i in iterator for i in s)
        return ans
        