class Solution:
    def maxDepth(self, s: str) -> int:
        # formula=number of left - number of right
        curr_depth=0
        max_depth=0 
        left=0
        right=0
        for i in s:
            if i=="(":
                curr_depth+=1
                max_depth=max(curr_depth,max_depth)
            elif i==")":
                curr_depth-=1
        return max_depth

        