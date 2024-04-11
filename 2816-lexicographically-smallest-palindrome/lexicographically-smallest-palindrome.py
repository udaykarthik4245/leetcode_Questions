class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        s=list(s)
        n=len(s)
        for i in range(n//2):
            if(s[i]!=s[n-i-1]):
                c=min(s[i],s[n-i-1])
                s[i],s[n-i-1]=c,c
        return ''.join(s)
        # another solution
        i = 0
        j = len(s) - 1
        s = list(s)

        while i <= j:
            if s[i] != s[j]:
                if s[i] < s[j]:
                    s[j] = s[i]
                else:
                    s[i] = s[j]

            i += 1
            j -= 1
        
        return "".join(s)
        
        