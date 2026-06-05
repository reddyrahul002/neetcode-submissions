class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        r_max,l_max=0,0
        fill=0
        while left<right :
            if height[left]<height[right]:
                l_max=max(l_max,height[left])
                fill+=l_max-height[left]
                left+=1
            elif height[right]<=height[left]:
                r_max =max(r_max, height[right])
                fill+=r_max-height[right]
                right-=1
        return fill



