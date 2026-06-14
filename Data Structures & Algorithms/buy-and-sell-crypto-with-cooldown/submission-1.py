class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<=1:
            return 0
        holding  = float('-inf')    
        sold     = float('-inf')  
        cooldown = 0  
        for price in prices:
            prev_holding  = holding
            prev_sold     = sold
            prev_cooldown = cooldown
            prev_holding  = holding
            holding= max(prev_holding,prev_cooldown-price)
            sold = prev_holding + price
            cooldown = max(prev_cooldown, prev_sold)
        return max(holding,sold,cooldown)
