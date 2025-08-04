class Solution:
    def maxDepth(self, s: str) -> int:
        # formula=number of left - number of right
        curr_depth=0
        max_depth=0 
        left=0
        right=0
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
                left+=1
                curr_depth=left-right
                max_depth=max(curr_depth,max_depth)
            elif i not in ("(",")"):
                curr_depth=left-right
                max_depth=max(curr_depth,max_depth)
            else:
                stack.append(i)
                right+=1
                curr_depth=left-right
                max_depth=max(curr_depth,max_depth)
        return max_depth

        