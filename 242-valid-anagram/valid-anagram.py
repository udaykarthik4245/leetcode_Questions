class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # else:
        #     s_l=list(s)
        #     t_l=list(t)
        #     s_l.sort()
        #     t_l.sort()
        #     if s_l==t_l:
        #         return True
        #     else:
        #         return False
        return Counter(s)==Counter(t)