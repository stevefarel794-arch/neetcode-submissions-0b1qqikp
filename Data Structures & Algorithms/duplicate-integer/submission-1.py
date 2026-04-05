class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in set(nums):
            d[i]=nums.count(i)
        for j in d.values():
            if j >1 :
                return True
        return False


        