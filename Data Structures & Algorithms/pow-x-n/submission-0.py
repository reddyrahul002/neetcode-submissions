class Solution:
    def myPow(self, x: float, n: int) -> float:
        product=1
        
        
            
        for i in range(abs(n)):
            product*=x
        return 1/product if n <0 else product