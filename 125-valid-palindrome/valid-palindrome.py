
# OPTIMAL SOLUTION  BINARY SEARCH 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left] == s[right] or s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        return True
        
                # Convert the string to lowercase and remove non-alphanumeric characters
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the cleaned string is a palindrome
        return cleaned_s == cleaned_s[::-1]
        # l=s.replace(",","")
        # w=l.replace(" ","")
        # print(w)
        # l=re.sub(r'[^a-zA-Z]', '', s)
        # l=l.lower()
        # n=len(l)
        # f=0
        # e=n-1
        # for i in range(len(l)):
        #     if l[i]!=l[e-f]:
        #         return False
        #         # break
        #     else:
        #         f+=1
        #         e-=1
        # return True

