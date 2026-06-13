class Solution:
    def rob(self, nums: List[int]) -> int:
        store={}
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        store={0:nums[0],1:max(nums[0],nums[1])}
        def mxM(x):
            if x in store:
                return store[x]
            store[x] = max(nums[x]+mxM(x-2),mxM(x-1))
            return store[x]
        return mxM(len(nums)-1)
        