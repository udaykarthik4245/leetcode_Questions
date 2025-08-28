class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        
        max_area=0
        while l<r:
            w=r-l
            h=min(height[l],height[r])

            area=w*h
            max_area=max(max_area,area)

            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_area