class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in present:
                return [present[diff],i]
            else:
                present[nums[i]]=i


                
            


        