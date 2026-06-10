class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result,sol=[],[]
        n=len(nums)

        def backtrack(start,sol):

            if start==n:
                result.append(sol[:])
                return

            
            backtrack(start+1,sol)

            sol.append(nums[start])
            backtrack(start+1,sol)
            sol.pop()

        backtrack(0,sol)

        return result

        