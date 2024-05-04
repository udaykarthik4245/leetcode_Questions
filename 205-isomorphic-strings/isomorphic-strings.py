class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=len(s)
        b=len(t)
        d={}
        for i in range(a):
            c1,c2=s[i],t[i]
            if c1 not in d:
                if c2 in d.values():
                    return False
                d[c1]=c2
            elif d[c1]!=c2:
                return  False
        return True
        