class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        s=list(s)
        # print(l)
        # first=0
        # last=len(l)-1
        # while first < last:
        #     if l==set[l]:
        #         if l[first] != l[last]:
        #             # Replace the character at last index with the character at first index
        #             l[first]=l[last]
        #             # l[last] = l[first]
        #     else:
        #         if l[first] != l[last]:
        #             l[last] = l[first]
        #         # Move the pointers inward
        #     first += 1
        #     last -= 1
        
        # # Join the modified list to form the smallest palindrome
        # return ''.join(l)
        # # return l
        n=len(s)
        for i in range(n//2):
            if(s[i]!=s[n-i-1]):
                c=min(s[i],s[n-i-1])
                s[i],s[n-i-1]=c,c
        return ''.join(s)
        
        