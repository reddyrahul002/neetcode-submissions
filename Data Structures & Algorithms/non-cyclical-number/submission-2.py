class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  
        while n!=1:
            if n in seen:                  
                return False
            seen.add(n)
            sumi = 0
            while n>0:
                digi = n%10
                sumi+=digi*digi
                n=n//10
            n=sumi
        return True
            

            
        