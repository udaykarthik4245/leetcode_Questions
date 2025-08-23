class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            res=0
            for i in range(len(piles)):
                
                res+=math.ceil(piles[i]/k)
            return res<=h
            
        # n=len(piles)
        # maxi=max(piles)
        l=1
        r=max(piles)
        # k_find=[x for x in range(1,max(piles)+1)]
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                r=mid-1
            else:
                l=mid+1
        return l