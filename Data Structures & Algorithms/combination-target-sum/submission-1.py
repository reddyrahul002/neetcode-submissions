class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result,sol=[],[]
        total=0
        n=len(nums)
        def backtrack(index,sol,total):

            if total==target:
                result.append(sol[:])
            if total > target:
                return   
            for i in range(index,n):
                sol.append(nums[i])
                backtrack(i,sol,total+nums[i])
                sol.pop()
        backtrack(0,sol,total)
        return result