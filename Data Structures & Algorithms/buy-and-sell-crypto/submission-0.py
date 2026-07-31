class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        c = len(prices)
        for i in range(0,c-1):
            k=prices[i]
            d=max(prices[i+1:])
            a = max(a,d-k)
        return a
   