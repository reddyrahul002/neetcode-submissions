class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        sol=[]

        def is_pali(s):
            return s==s[::-1]

        def backtrack(start):
            if start==len(s):
                res.append(sol[:])
                return
            
            for i in range(start,len(s)):
                sub=s[start:i+1]
                if is_pali(sub):
                    sol.append(sub)
                    backtrack(i+1)
                    sol.pop()
        backtrack(0)
        return res