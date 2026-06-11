from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        sol=[]
        n=len(nums)
        nums.sort()
        def backtrack(start,sol):
            if start==n:
                result.append(sol[:])
                return
            sol.append(nums[start])
            backtrack(start+1,sol)
            sol.pop()
            
            while  start+1<n  and nums[start]==nums[start+1] :
                start+=1
            backtrack(start+1,sol)
        
        backtrack(0,sol)
        return result



