class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        mina=prices[0]
        mx=0
        for i in prices:
            mina=min(mina,i)
            mx=max(mx,i-mina)
        return mx

        # for i in range(prices.index(mina)+1,len(prices)):
        #     mx=max(mx,prices[i])
        # if mx-mina<0:
        #     return (0)
        # else:

        #     return(mx-mina)