class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        res=0
        m=1
        l=[]
        l.append(s[0])
        for c in s[1:]:
            if(not(c in l)):
                l.append(c)
                m+=1
            else:
                res=max(res,m)
                while c in l:
                    l=l[1:]
                l.append(c)
                m=len(l)
        res = max(res,m)
        return res
