class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            s='ù'
            return s
        else:
            s=f"{len(strs[0])}"+"#"+strs[0]
            for i in range(1,len(strs)):
                s+=f'{len(strs[i])}'+"#"+strs[i]

            return s

    def decode(self, s: str) -> List[str]:
        if s=='ù':
            return []
        else:
            l=[]
            i = 0
            while i < len(s):
                j = s.find('#', i)
                length = int(s[i:j])
                l.append(s[j+1 : j+1+length])
                i = j + 1 + length
            return l
