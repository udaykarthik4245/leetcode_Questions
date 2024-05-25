class Solution:
    def spiralOrder(self, arr: List[List[int]]) -> List[int]:
        ans=[]
        if len(arr) == 0 or len(arr[0]) == 0:
            return ans
        m=len(arr)
        n=len(arr[0])
        t=0
        b=m-1
        l=0
        r=n-1
        # ans=[]
        while t<=b and l<=r:
            for k in range(l,r+1):
                ans.append(arr[t][k])
            t+=1
            if t<=b:
                for k in range(t,b+1):
                    ans.append(arr[k][r])
                r-=1
            if l<=r and t<=b:
                for k in range(r,l-1,-1):
                    ans.append(arr[b][k])
                b-=1
            if t<=b and l<=r:

                for k in range(b,t-1,-1):
                    ans.append(arr[k][l])
                l+=1
        return ans
