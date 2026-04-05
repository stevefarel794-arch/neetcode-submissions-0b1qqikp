class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L=[]
        for x in strs:
            M=[]
            for j in strs:
                a=1
                if len(x)==len(j):
                    for i in range(len(x)):
                        if x[i] not in j or x.count(x[i])!=j.count(x[i]):
                            a=0
                            break

                    if a==1:
                        M.append(j)
            L.append(M)
        return [list(P) for P in set(tuple(M) for M in L)]
            
