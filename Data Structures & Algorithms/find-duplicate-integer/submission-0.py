class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        seen=set()
        while left<=right:
            if nums[left] in seen:
                return nums[left]
            
            seen.add(nums[left])
            left+=1
            
            
            


            
        