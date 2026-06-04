class Solution:
    def isPalindrome(self, s: str) -> bool:
        stng = s.strip().lower()
        i,j=0,len(stng)-1
        while(i<j):
            if not stng[i].isalnum() :
                i=i+1
                continue
            if not stng[j].isalnum():
                j=j-1
                continue
            if stng[i]==stng[j]:
                i,j=i+1,j-1
                continue
            else:
                return False
        return True
            



