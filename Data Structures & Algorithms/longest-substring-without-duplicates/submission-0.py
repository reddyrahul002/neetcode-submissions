class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        length=0
        present=set()

        for r in range(len(s)):
            while s[r] in present:
                present.remove(s[l])
                l+=1
            present.add(s[r])
            length=max(length,r-l+1)
            
        return length
                