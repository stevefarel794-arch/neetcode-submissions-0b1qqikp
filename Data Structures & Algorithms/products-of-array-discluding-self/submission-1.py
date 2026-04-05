import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=[]
        n=math.prod([c for c in nums if c!=0])
        for i in range(0,len(nums)):
            k=nums[:]
            k.pop(i)
            if 0 in k:
                L.append(0)
            elif nums[i]==0:
                L.append(int(n))
            else:
                L.append(int(n/nums[i]))
        return L
