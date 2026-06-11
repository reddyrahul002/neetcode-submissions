class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, sol = [], []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(start):
            if start==len(digits):
                res.append("".join(sol[:]))
                return
            
            for char in phone[digits[start]]:
                sol.append(char)
                backtrack(start+1)
                sol.pop()
            

        if digits:
            backtrack(0)

        return res

