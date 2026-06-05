class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        if k>len(s2):
            return False
        def fq_cnts(arr):
            result = {}
            for ch in arr:
                result[ch] = result.get(ch, 0) + 1
            return result
        s1_fq = fq_cnts(s1)
        s2_fq = fq_cnts(s2[:k])
        if s1_fq == s2_fq:
            return True
        for i in range(k,len(s2)):
            s2_fq[s2[i]]=s2_fq.get(s2[i],0)+1
            s2_fq[s2[i-k]]-=1
            if s2_fq[s2[i-k]] ==0:
                del s2_fq[s2[i-k]]
            if s1_fq == s2_fq:
                return True
        return False
            
                

            
                
            

            
            
            
