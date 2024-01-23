class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                duplicates += 1
            else:
                nums[i - duplicates] = nums[i]

        return len(nums) - duplicates
    #     arr.sort()
    #     n=len(arr)
    
    # # Initialize an empty list to store unique elements
    #     unique_arr = []

    #     # Iterate through the sorted list and add unique elements to the new list
    #     for i in range(n):
    #         if i == 0 or arr[i] != arr[i - 1]:
    #             unique_arr.append(arr[i])

    #     # Copy the unique elements back to the original list
    #     for i in range(len(unique_arr)):
    #         arr[i] = unique_arr[i]

    #     return len(unique_arr)
