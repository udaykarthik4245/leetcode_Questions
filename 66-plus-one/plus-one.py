class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        z=''.join(map(str,digits))
        i=int(z)+1
        return list(map(int,str(i)))
        