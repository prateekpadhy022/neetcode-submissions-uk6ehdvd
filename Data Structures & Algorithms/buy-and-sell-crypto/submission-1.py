class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        res, pr = 1,0

        while l < len(prices) and r < len(prices):
            if (prices[r]-prices[l]) < 0:
                l = r
                r = r+1
            elif (prices[r]-prices[l]) >= 0:
                res = prices[r]-prices[l]
                r = r+1
                if res > pr:
                    pr = res
            
                
        return pr



