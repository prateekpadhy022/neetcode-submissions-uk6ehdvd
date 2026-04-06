class Solution:
    def maxProfit(self, s: List[int]) -> int:
        l = 0
        r = l+1
        profit = 0
        while r < len(s):
            if s[l] < s[r]:
                
                profit = max(profit,(s[r] - s[l]))
                r += 1
            else:
                l = r
                r = l+1
        return profit
                
            
                



