class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if n<3:
            return False
        peak=arr.index(max(arr))  
        if peak==0 or peak==n-1:
            return False

        for i in range(peak):
            if arr[i]>=arr[i+1]:
                return  False
        for j in range(peak,n-1):
            if arr[j]<=arr[j+1]:
                return False
        return True

        # another solution

        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1
