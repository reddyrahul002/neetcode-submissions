class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordset=set(wordDict)
        memo={}
        def canbreak(start):
            if start==len(s):
                return True
            if start in memo:
                return memo[start]
            for i in range(start+1,len(s)+1):
                word=s[start:i]
                if word in wordset and canbreak(i):
                    memo[start]=True
                    return True
            memo[start]=False
            return False
        
        return canbreak(0)
        
            

        