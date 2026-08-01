class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = prices[0]
        c=0
        for price in prices[1:]:
            if(price < a):
                a = price
            else:
                c = max(c,price - a)
        return c
   