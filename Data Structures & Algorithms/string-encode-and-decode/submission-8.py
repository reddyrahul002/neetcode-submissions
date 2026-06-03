class Solution:

    def encode(self, strs: List[str]) -> str:
        
        stng=''
        for i in strs:
            stng+=str(len(i))+'#'+i
        return stng

    def decode(self, s: str) -> List[str]:
        final =[]
        i=0;
        while i < len(s):
            j=i
            while  s[j] !="#":
                j+=1
            length = int(s[i:j])
            
            final.append(s[j+1:j+1+length])
            i=j+length+1
        
        return final
