import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        min_k = r
        while(l<=r):
            hours=0
            mid=(l+r)//2

            for i in piles:
                hours+=math.ceil(i/mid)
            if hours <=h:
                min_k=min(min_k,mid)
                r=mid-1
            else:
                l =mid+1
        return min_k

