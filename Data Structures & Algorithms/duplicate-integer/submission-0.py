class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        present = {}
        for i in nums:
            if i in present:
                return True
            else :
                present[i]=1;
        return False