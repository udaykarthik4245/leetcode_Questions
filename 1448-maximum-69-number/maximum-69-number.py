class Solution:
    def maximum69Number (self, num: int) -> int:
        i=-1
        nums=str(num)
        for j in range(len(nums)):
            if nums[j]=="6":
                i=j
                break
        if i==-1:
            return num
        else:
            return int(nums[:i]+'9'+nums[i+1:])

        