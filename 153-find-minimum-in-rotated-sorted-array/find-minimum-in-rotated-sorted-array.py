class Solution:
    def findMin(self, arr: List[int]) -> int:
        # return min(nums)
        low=0
        ans=arr[0]
        n=len(arr)
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if arr[low]<=arr[mid]:
                ans=min(arr[low],ans)
                low=mid+1
            else:
                high=mid-1
                ans=min(arr[mid],ans)
                
        return ans


        