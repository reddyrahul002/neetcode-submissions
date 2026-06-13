class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0

        if len(s)==1:
            return 1


        for k in range(len(s)):
            i,j=k,k
            while i>=0 and j<len(s) and s[i]==s[j]:
                count+=1
                i-=1
                j+=1

            i,j=k,k+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                count+=1
                i-=1
                j+=1
        
        return count

