class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    

  
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l<r:

            while l<r and not self.alfnum(s[l]):
                l+=1

            while r>l and not self.alfnum(s[r]):
                r-=1

            if s[l].lower() != s[r].lower():
                return False
            r-=1
            l+=1

        return True


    def alfnum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or 
                ord('1') <= ord(c) <= ord('9'))
