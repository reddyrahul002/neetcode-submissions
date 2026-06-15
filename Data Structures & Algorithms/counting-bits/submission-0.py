class Solution:
    def countBits(self, n: int) -> List[int]:
        out=[]

        for i in range(0,n+1):
            s=i
            count=0
            while s:
                s&=s-1
                count+=1
            out.append(count)
        return out


        