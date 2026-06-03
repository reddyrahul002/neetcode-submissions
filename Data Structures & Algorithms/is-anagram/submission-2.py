class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        present1 = {}
        present2 = {}
        for i in s:
            if i in present1:
                present1[i]+=1 
            else :
                present1[i]=1    
        for j in t:
            if j in present2:
                present2[j]+=1  
            else :
                present2[j]=1    
        
        for i in present1.keys():
            if i in present2 and present1[i]== present2[i]:
                continue
            else:
                return False

        for j in present2.keys():
            if j in present1 and present1[i]== present2[i]:
                continue
            else:
                return False
        return True


