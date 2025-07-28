class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(1,len(s)+1):
            s_r=s[i:]+s[:i]
            if s_r==goal:
                return True
        return False 
        