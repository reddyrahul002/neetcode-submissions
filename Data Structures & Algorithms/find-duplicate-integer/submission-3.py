class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
                
            
            


            
        