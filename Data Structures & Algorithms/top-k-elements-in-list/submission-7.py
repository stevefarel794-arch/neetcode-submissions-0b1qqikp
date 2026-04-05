class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set=set(nums)
        d={}
        t=[]
        for c in nums_set:
            d[c]=nums.count(c)
        l=d.values()
        l=sorted(l,reverse=True)
        i=0
        while k!=0 and i<len(l):
            for c in nums_set:
                if (c in t) == False:
                    if d[c]==l[i]:
                        t.append(c)
                        k=k-1
            i=i+1
        return t



  
