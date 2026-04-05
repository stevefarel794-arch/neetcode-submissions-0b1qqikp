import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=[]
        for i in range(0,len(nums)):
            k=nums[:]
            k.pop(i)
            if 0 in k:
                L.append(0)
            else:
                L.append(math.prod(k))
        return L
