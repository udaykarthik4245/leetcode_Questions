class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_d=int(a,2)
        b_d=int(b,2)
        # print(a_d,b_d)
        c=a_d+b_d
        res=bin(c)
        return(res[2:])
        