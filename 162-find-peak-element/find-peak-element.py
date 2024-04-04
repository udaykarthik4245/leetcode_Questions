class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        low=1
        high=n-2
        if(n==1):
            return 0
        if(nums[0]>nums[1]):
            return 0
        if(nums[-1]>nums[-2]):
            return n-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            elif(nums[mid]>nums[mid-1]):
                low=mid+1
            else:
                high=mid-1
        return -1
    #another solution 
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1 # Narrow it since it wont be a smaller number
            else: #arr[mid] > arr[mid + 1]
                right = mid # Could be Right
        
        return left

    #o(n) solution
        return nums.index(max(nums))
            

        