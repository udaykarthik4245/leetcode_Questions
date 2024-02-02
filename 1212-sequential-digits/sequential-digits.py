class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        r=[]
        for i in range(1,9):
            while i<=high and i%10!=0:
                if i>=low:
                    r.append(i)
                i=(i*10)+(i%10)+1
        return sorted(r)

        