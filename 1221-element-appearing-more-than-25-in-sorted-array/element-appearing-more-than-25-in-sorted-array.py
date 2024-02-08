from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # for i in range(len(arr)):
        c=Counter(arr)
        # print(c)
        # print(c.most_common(1))
        return(c.most_common(1)[0][0])
                