class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # word=s.split()
        # if not word:
        #     return 0
        return len(s.split()[-1])
        