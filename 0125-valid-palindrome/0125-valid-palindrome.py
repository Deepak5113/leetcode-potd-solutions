class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        t=''
        for i in s:
            if(i.isalnum()):
                t+=i
        return t[::]==t[::-1]
        