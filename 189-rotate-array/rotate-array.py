class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # """
        k%=len(nums)
        first=nums[-k:]
        nums[:]=nums[:-k]
        nums[:0]=first
