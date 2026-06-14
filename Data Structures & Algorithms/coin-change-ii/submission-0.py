class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        coins.sort()
        def f(amt,i):
            if amt == 0: return 1
            if amt < 0 or i == len(coins):
                return 0  
            if (amt, i) in memo:
                return memo[(amt, i)]   
            memo[(amt, i)] = f(amt - coins[i], i) + f(amt, i+1)
            return memo[(amt, i)]
        
        return f(amount,0)
        

            

        