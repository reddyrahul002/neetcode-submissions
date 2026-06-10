class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result,sol=[],[]
        n=len(nums)

        def backtrack(index,sol):
            if sum(sol)==target:
                result.append(sol[:])
            if sum(sol) > target:
                return   
            
            for i in range(index,n):
                sol.append(nums[i])
                backtrack(i,sol)
                sol.pop()

        backtrack(0,sol)

        return result