class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
                # # Initialize a pointer for the current position
        # current = 0

        # # Iterate through the list
        # while current < len(nums):
        #     if nums[current] == val:
        #         # If the current element is equal to val, remove it
        #         nums.pop(current)
        #     else:
        #         # If the current element is not equal to val, move to the next element
        #         current += 1

        # # Return the new length of the list
        # return len(nums)
                                          # same as 2nd approach
        # while i<len(nums):
        #     if nums[i]==val:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)
