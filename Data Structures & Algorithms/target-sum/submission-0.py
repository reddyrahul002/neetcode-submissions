class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}

        def backtrack(i,c_sum):
            if i==len(nums):
                return 1 if c_sum ==target else 0
            if (i,c_sum) in memo:
                return memo[(i,c_sum)]
            addi =  backtrack(i+1,c_sum+nums[i])
            subi =  backtrack(i+1,c_sum-nums[i])
            memo[(i, c_sum)] = addi+subi
            return memo[(i, c_sum)]
        
        return backtrack(0,0)
