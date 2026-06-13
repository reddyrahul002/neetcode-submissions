class Solution:
    def longestPalindrome(self, s: str) -> str:

        reslen=0
        res=''

        for k in range(len(s)):
            # odd length
            i,j=k,k
            while i>=0 and j<len(s) and s[i]==s[j]:
                if reslen < j-i+1:
                    res=s[i:j+1]
                    reslen=j-i+1
                i-=1
                j+=1
            # even length
            i,j=k,k+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                if reslen < j-i+1:
                    res=s[i:j+1]
                    reslen=j-i+1
                i-=1
                j+=1
        return res

            
            
                
        
