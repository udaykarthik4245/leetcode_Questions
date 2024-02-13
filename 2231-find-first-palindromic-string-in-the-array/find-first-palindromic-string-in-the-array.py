class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        # if not words :
        #     return("")
        for i in words:
            if i==i[::-1]:
                return(i)
                break
            # else:
        return ("")