class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        profit=0

        for r in range(len(prices)):
            
            while prices[left]>prices[r]:
                left+=1

            profit=max(profit,prices[r]-prices[left])

        return profit

        