class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l=[]
        for c in s:
            if c.isalnum():
                l.append(c)
        a=list(reversed(l))
        if l==a:
            return True
        else:
            return False