class Solution:
    def largestOddNumber(self, num: str) -> str:
        # nums=int(num)
        #1solution

        num=list(map(int,num))
        if num[-1]%2!=0:
            return ''.join(map(str,num))
        
        for i in range(len(num) - 1, -1, -1):
            if num[i] % 2 != 0:
                return ''.join(map(str, num[:i + 1]))
        
        # No odd digit found
        return ""
        # 2nd solution


        # for i in range(len(num)-1,-1,-1):
        #     if int(num[i])%2!=0:
        #         return num[:i+1]
        # return ''
            
        