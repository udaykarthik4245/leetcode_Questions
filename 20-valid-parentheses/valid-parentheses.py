class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in d.keys():
                st.append(i)
            else:
                if not st:
                    return False
                else:
                    poped=st.pop()
                    if d[poped]!=i:

                        return False
        return not st

# #2nd solution
#         open_close = dict(('()', '[]', '{}'))

#         st = []
        
#         for idx in s:

#                 if idx in '([{':
#                     st.append(idx)

#                 elif len(st) == 0 or idx != open_close[st.pop()]:
#                     return False

#         return len(st) == 0

        