class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result,sol=[],[]
        n=len(nums)
        def backtrack(start,sol):
            # if start==n:
            result.append(sol[:])
                # return
                
            for i in range(start,len(nums)):
                sol.append(nums[i])
                backtrack(i+1,sol)
                sol.pop()
        backtrack(0,sol)

        return result

        