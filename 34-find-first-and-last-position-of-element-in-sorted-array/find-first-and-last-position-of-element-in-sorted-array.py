class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def first(nums,target):
            first_index = -1
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first_index = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first_index

        def last(nums,target):
            last_index = -1
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last_index = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last_index

        return (first(nums,target), last(nums,target))