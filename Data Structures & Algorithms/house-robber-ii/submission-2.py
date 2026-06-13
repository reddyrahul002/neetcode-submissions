class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)

        if len(nums) == 1:
            return nums[0]
        

        def rob(houses):
            h=len(houses)
            if h==0:
                return 
            if h==1:
                return houses[0]
            store={0:houses[0],1:max(houses[0],houses[1])}

            def mH(x):
                if x in store:
                    return store[x]
                store[x]=max(houses[x]+mH(x-2),mH(x-1))
                return store[x]
            return mH(h-1)
        
        return max(rob(nums[1:]),rob(nums[:-1]))
            
        

