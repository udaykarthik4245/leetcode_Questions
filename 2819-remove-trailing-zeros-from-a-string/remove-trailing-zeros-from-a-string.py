class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        l=list(num)
        # l.reverse()
        # print(l)
        n=len(l)
        first=n-1
        # i=n-1
        # count=0
        while first>=0 and l[first] == '0':
            # count+= 1
            first-=1
            
        if first == -1:
            return '0'  # if the number is all zeros, return '0'
        else:
            return ''.join(l[:first + 1])



        