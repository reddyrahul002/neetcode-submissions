class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        l_sum =nums[0]

        for i in range(1,len(nums)):
            l_sum=max(nums[i],nums[i]+l_sum)
            max_sum=max(l_sum,max_sum)
        return max_sum
    


        
        