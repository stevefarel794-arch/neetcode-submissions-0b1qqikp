class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        l=set(nums)
        a=0
        for b in l:
            if (b - 1) not in l:
                current_num = b
                current_streak = 1
                while (current_num + 1) in l:
                    current_num += 1
                    current_streak += 1
                if current_streak > a:
                    a = current_streak
        return a