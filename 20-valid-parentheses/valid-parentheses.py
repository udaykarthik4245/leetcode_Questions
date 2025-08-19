class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={'}':'{',')':'(',']':'['}
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped_ele=stack.pop()
                    if popped_ele not in d[i]:
                        return False
        return not stack
        