class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,length,maxcount,count=0,0,0,{}
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0) +1
            maxcount = max(maxcount,count[s[r]])
            while r-l+1 - maxcount >k:
                count[s[l]]-=1
                l+=1
            length =max(length,r-l+1)
        return length
        
        