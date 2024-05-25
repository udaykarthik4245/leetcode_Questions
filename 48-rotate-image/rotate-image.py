class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(arr)
        for i in range(n):
            for j in range(n):
                if i<j:
                    arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
                    # upto here we get the transpose of the matrix

        for i in range(n):
            arr[i]=arr[i][::-1]
        # return arr