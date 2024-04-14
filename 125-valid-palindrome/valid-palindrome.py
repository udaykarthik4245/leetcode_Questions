class Solution:
    def isPalindrome(self, s: str) -> bool:
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

