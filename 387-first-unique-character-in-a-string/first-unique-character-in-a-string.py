class Solution:
    def firstUniqChar(self, s: str) -> int:
        sl=list(s)
        du=[]


        # for i in sl:
        #     if sl.count(i)==1:
        #         du.append(i)
        #     else:
        #         continue
        # if len(du)>0:

        #     return(s.index(du[0]))
        # else:
        #     return -1
        count = Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i 
        return -1
            
                
        