class Solution:
    def trap(self, height: List[int]) -> int:
        s=0
        max_left=[]
        max_right=[]
        c = len(height)
        if c < 3:
            return 0
        for i in range(1,c-1):
            max_right.append(max(height[i+1:]))
            max_left.append(max(height[0:i]))
            d = height[i]
            a=min(max_left[i-1],max_right[i-1])
            if(a>d):
                s+=a-d
        return s