class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in haystack:
        n=len(needle)
        # s=haystack.split()
        # cus_len=[n]
        # output=[]
        startindex=0
        if not needle:
            return 0
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n]==needle:
                return i
            # else:
        return -1



        