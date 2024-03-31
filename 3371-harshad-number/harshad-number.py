class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        l=[int(i) for i in str(x)]
        # print(l)
        s=sum(l)
        # print(s)
        if x%s==0:
            return s
        else:
            return -1
        