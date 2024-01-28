class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        n=len(s)
        # l=l[::-1]
        # z=' '.join(map(str,l))
        # # sr=str(z)
        # return(z)  
        for i in range(n//2):
            s[i],s[n-i-1]=s[n-i-1],s[i]
            # i+=1
        z=' '.join(map(str,s))
        return z

        