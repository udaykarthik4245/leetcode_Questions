class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)
        nums1=nums[:n//2]
        nums2=nums[n//2:]
        print(nums1)
        print(nums2)
        res=[]
        for i in range(len(nums1)):
            res.append(nums1[i])
            res.append(nums2[i])
        return res

        # easy solution
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res