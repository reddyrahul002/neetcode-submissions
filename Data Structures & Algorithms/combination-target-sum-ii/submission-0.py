class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result=[]
        sol=[]
        n=len(candidates)
        candidates.sort()
        total=0

        def backtrack(start,sol,total):
            
            if total==target:
                result.append(sol[:])
                return
            if total > target or start == n:
                return  

            sol.append(candidates[start])
            backtrack(start+1,sol,total+candidates[start])
            sol.pop()

            while  start+1<n  and candidates[start]==candidates[start+1] :
                start+=1
            backtrack(start+1,sol,total)

        backtrack(0,sol,total)
        return result