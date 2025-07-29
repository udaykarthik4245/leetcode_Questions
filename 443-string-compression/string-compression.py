from collections import Counter
class Solution:
    def compress(self, s: List[str]) -> int:
        res=[]
        count=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                res.append(s[i-1])
                if count>1:
                    res.extend(list(str(count)))

                count=1
        res.append(s[-1])
        if count>1:
            res.extend(list(str(count)))
        for i in range(len(res)):
            s[i]=res[i]
        return len(res)