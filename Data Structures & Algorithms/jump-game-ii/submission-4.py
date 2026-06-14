class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        goal=n-1
        jumps=0
        while goal>0:
            for i in range(n):
                if i+nums[i]>=goal:
                    goal=i
                    jumps+=1
                    break
            
        return jumps

